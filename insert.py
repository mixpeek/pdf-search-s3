import boto3
from tika import parser
from opensearchpy import OpenSearch
from config import *
import sys


# elasticsearch object
os = OpenSearch(opensearch_uri)

s3_file_name="prescription.pdf"
bucket_name="mixpeek-demo"


def download_file():
    """Download the file
    :param str s3_file_name: name of s3 file
    :param str bucket_name: bucket name of where the s3 file is stored
    """

    # s3 boto3 client instantiation
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    # open in memory
    with open(s3_file_name, 'wb') as file:
        s3_client.download_fileobj(
            bucket_name,
            s3_file_name,
            file
        )
        print("file downloaded")
        # parse the file
        parsed_pdf_content = parser.from_file(s3_file_name)['content']
        print("file contents extracted")
        # insert parsed pdf content into elasticsearch
        insert_into_search_engine(s3_file_name, parsed_pdf_content)
        print("file contents inserted into search engine")


def insert_into_search_engine(s3_file_name, parsed_pdf_content):
    """Download the file
    :param str s3_file_name: name of s3 file
    :param str parsed_pdf_content: extracted contents of PDF file
    """
    doc = {
        "filename": s3_file_name,
        "parsed_pdf_content": parsed_pdf_content
    }
    # insert
    resp = os.index(
        index = index_name,
        body = doc,
        id = 1,
        refresh = True
    )
    print('\nAdding document:')
    print(resp)


def create_index():
    """Create the index
    """
    index_body = {
        'settings': {
            'index': {
                'number_of_shards': 1
            }
        }
    }
    response = os.indices.create(index_name, body=index_body)
    print('\nCreating index:')
    print(response)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
