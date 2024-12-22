from flask import Blueprint, jsonify
import logging

api = Blueprint('api', __name__)
logging.basicConfig(level=logging.DEBUG)

@api.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Welcome to the API"}), 200

# You can add new routes here when needed
