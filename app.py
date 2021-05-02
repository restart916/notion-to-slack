import os
from notion.client import NotionClient
from flask import Flask
from flask import request

app = Flask(__name__)

token = ""
url = ''


def test(token, url):
    # notion
    client = NotionClient(token_v2=token)
    cv = client.get_collection_view(url, collection=None, force_refresh=True)
    # row = cv.collection.add_row()
    print(row)

    row.Name = 'wonderful python'


@app.route('/test', methods=['GET'])
def getTest():
    test(token, url)
    return f'added to Notion'

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)