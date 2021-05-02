import logging
import os

import requests
from notion.client import NotionClient

logging.basicConfig(level=logging.DEBUG)

notion_token = os.environ.get("NOTION_TOKEN")
notion_url = os.environ.get("NOTION_URL")
slack_url = os.environ.get("SLACK_URL")


def send_slack(row, slack_url):
    page_id = ''.join(row.id.split('-'))
    link = f'https://www.notion.so/{page_id}'

    payload = {
        'username': '구독 UI/UX', 
        'icon_emoji': ':postbox:',
        'blocks': [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"새 글이 올라왔어요!\n제목: {row.Name}\n분류: {row.Tag}\n<{link}|보러가기>"
                },
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "image",
                    "emoji": True
                },
                "image_url": row.Cover[0],
                "alt_text": "image"
            }
        ]
    }

    res = requests.post(slack_url, json=payload)
    print(res.status_code)
    print(res.text)
    
def update_item(item):
    item.Send = True

def get_new_items(token, notion_url):
    # notion
    client = NotionClient(token_v2=token)
    cv = client.get_collection_view(notion_url, collection=None, force_refresh=True)

    return list(filter(lambda row: row.Send == False, cv.collection.get_rows()))
            

items = get_new_items(notion_token, notion_url)

for item in items:
    send_slack(item, slack_url)
    update_item(item)