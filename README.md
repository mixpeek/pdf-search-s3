
# Text Search of PDF files in S3 bucket(s) using Tika and OpenSearch

Using Tika and OpenSearch to search the contents of PDF files across S3 bucket(s)

[Medium Article Tutorial](https://medium.com/@mixpeek/search-text-from-pdf-files-stored-in-an-s3-bucket-2f10947eebd3)

### Installation

OpenSearch:
```bash
brew update
brew install opensearch
opensearch
```

App dependencies:
```python
pip install -r requirements.txt
```

### Setup

- Add your AWS keys to `config.py`
- Provide the filename you want to search in `insert.py`'s variable: `s3_file_name`


### Run
1. Create the index by running `python insert.py create_index`
2. Download the file, extract the contents then insert it into OpenSearch via `python insert.py download_file`
3. Run the app via `python app.py`
