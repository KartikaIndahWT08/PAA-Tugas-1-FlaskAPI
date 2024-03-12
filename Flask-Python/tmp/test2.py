#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'Kartika Indah',
                    'email': 'kartikaindahwt@gmail.com'})

app.run()