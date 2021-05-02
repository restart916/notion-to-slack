import os
from notion.client import NotionClient

token = os.environ.get("TOKEN")
url = os.environ.get("URL")

def test(token, url):
    # notion
    client = NotionClient(token_v2=token)
    cv = client.get_collection_view(url, collection=None, force_refresh=True)

    for row in cv.collection.get_rows():
        if row.Send == False:
            row.Send = True
            print(row)

test(token, url)
