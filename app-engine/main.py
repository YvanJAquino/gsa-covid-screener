import json
from datetime import datetime
from uuid import uuid4
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import pubsub_v1
import os

app = Flask(__name__)

publisher = pubsub_v1.PublisherClient()
project_id = os.environ.get('PROJECT_ID')
topic_id = os.environ.get('TOPIC')
topic_name = f'projects/{project_id}/topics/{topic_id}'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def handle_post():    
    data = request.form.to_dict()
    headers = request.headers
    ipaddr = headers.get('X-Appengine-User-Ip')
    latlong = headers.get('X-Appengine-Citylatlong')
    now = datetime.now()
    result = 'RED' if 'none' not in data.keys() else 'GREEN'
    # https://developers.login.gov/attributes/
    user = {
        'iss': str(now),
        'sub': str(uuid4()),
        'email': 'example@example.com',
        'ial': 'urn:aarp:323:5642',
        'aal': 'urn:rars:325:5724',
        'res': result,
        'ipa': str(ipaddr),
        'loc': str(latlong)
    } 
    publisher.publish(topic_name, json.dumps(user).encode())
    return json.dumps(user, indent=2)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
