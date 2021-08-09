import json
import base64
from google.cloud import bigquery
import os

bq = bigquery.Client()
table_id = os.environ.get('TABLE_ID')

def ps2bq(event, context):
    
    if 'data' in event:
        data: str = base64.b64decode(event['data']).decode('utf-8')
        data: dict = json.loads(data)
    bq.insert_rows_json(table_id, [data])

    print(json.dumps(data))