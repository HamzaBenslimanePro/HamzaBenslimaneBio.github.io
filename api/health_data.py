from flask import Blueprint, jsonify
from pymongo import MongoClient

health_data_bp = Blueprint('health_data', __name__)

# MongoDB setup
client = MongoClient('localhost', 27017)
db = client.health_monitoring
health_data_collection = db.health_data

@health_data_bp.route('/', methods=['GET'])
def get_health_data():
    # Logic to return historical health data
    data = list(health_data_collection.find())
    return jsonify(data)

@health_data_bp.route('/', methods=['POST'])
def add_health_data():
    # Logic to submit new health data
    new_data = request.json
    health_data_collection.insert_one(new_data)
    return jsonify({'message': 'Data added successfully'})
