import os
import datetime
import requests
from functools import wraps
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

base_url = os.getenv('OKTA_ISSUER')
client_id = os.getenv('OKTA_CLIENT_ID')
client_secret = os.getenv('OKTA_CLIENT_SECRET')


def okta_jwt_required(func):
    @wraps(func)
    def check_authorization(*args, **kwargs):
        bearer_token = request.headers.get("Authorization")
        print("Got token {}".format(bearer_token))
        token = bearer_token.replace('Bearer ', '')
        introspect_url = base_url + '/v1/introspect'
        introspect_payload = {
            'token': token,
            'token_type_hint': 'access_token',
            'client_id': client_id,
            'client_secret': client_secret
        }
        response = requests.post(introspect_url, data=introspect_payload)
        print("Introspection response {}".format(response.json()))
        if response.json().get('active'):
            return func()
        else:
            return Response('JWT Authorization Failed', 401, {})

    return check_authorization


@app.route('/api/messages')
@okta_jwt_required
def messages():
    print(request.headers)
    message_list = [
        {'id': 1,
         'date': datetime.datetime.now().isoformat(),
         'text': 'Hello world!'},
        {'id': 2,
         'date': datetime.datetime.now().isoformat(),
         'text': 'Go Warriors!'}
    ]
    return jsonify({'messages': message_list})


@app.route('/')
def index():
    return 'Index Page'
