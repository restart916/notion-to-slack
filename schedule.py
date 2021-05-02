import logging
import os

import requests
from notion.client import NotionClient
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)

notion_token = os.environ.get("NOTION_TOKEN")
notion_url = os.environ.get("NOTION_URL")
slack_url = os.environ.get("SLACK_URL")


def send_slack(row, slack_url):
    # print(row.Name)    

    payload = {
        'channel': '#random', 
        'username': 'webhookbot', 
        'text': f'New item added! {row.Name}', 
        'icon_emoji': ':ghost:'
    }

    res = requests.post(slack_url, json=payload)
    # print(res.status_code)
    # print(res.text)
    
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