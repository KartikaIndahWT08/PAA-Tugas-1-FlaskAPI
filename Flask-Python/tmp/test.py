#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'Kartika Indah',
                       'email': 'kartikaindahwt@gmail.com'})
app.run()