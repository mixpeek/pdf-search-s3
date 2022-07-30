from flask import Flask, jsonify, request
from opensearchpy import OpenSearch
from config import *

app = Flask(__name__)
os = OpenSearch(opensearch_uri)


@app.route('/search', methods=['GET'])
def search_file():
    # value from the api
    query = request.args.get('q', default = None, type = str)

    # query payload to ES
    payload = {
        'query': {
            'match': {
                'parsed_pdf_content': query
            }
        }
    }
    # response
    response = os.search(
        body=payload,
        index=index_name
    )

    return jsonify(response)


if __name__ == '__main__':
    app.run(host="localhost", port=5011, debug=True)
