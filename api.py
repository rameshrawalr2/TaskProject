#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 18:32:52 2018

@author: ramesh
"""
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_csv():
    submitted_file = request.files['file']
    content =submitted_file.read()
    print(content)
    return "blank"
if __name__ == "__main__":
    app.run()
