#!/usr/bin/python3
'''
    This module contains variable and methods used to connect to API
'''
import os
from models import storage
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={'/*': {'origins': '0.0.0.0'}})
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))


@app.teardown_appcontext
def teardown_appcontext(code):
    '''
        Handles teardown
    '''
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    '''
        Returns a JSON-formatted error response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
