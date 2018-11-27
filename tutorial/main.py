import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None

# TODO: Authorization Step 1: Launch Smartcar authorization dialog


@app.route('/login', methods=['GET'])
def login():
    # TODO: Authorization Step 1: Launch Smartcar authorization dialog


@app.route('/exchange', methods=['GET'])
def exchange():
    # TODO: Authorization Step 3: Handle Smartcar response

    # TODO: Request Step 1: Obtain an access token


@app.route('/vehicle', methods=['GET'])
def vehicle():
    # TODO: Request Step 2: Get vehicle ids

    # TODO: Request Step 3: Create a vehicle

    # TODO: Request Step 4: Make a request to Smartcar API


if __name__ == '__main__':
    app.run(port=8000)
