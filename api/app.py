import json
import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/api/messages')
def messages():
    return {'messages': []}


@app.route('/')
def index():
    return 'Index Page'
