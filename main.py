import os

from flask import Flask, request
from notion.client import NotionClient

app = Flask(__name__)

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

@app.route('/test', methods=['GET'])
def getTest():
    test(token, url)
    return f'added to Notion'

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)