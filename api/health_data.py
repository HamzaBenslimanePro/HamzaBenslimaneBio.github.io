from flask import Blueprint, request, jsonify
from pymongo import MongoClient

health_data_bp = Blueprint('health_data', __name__)

# MongoDB setup
client = MongoClient(app.config['MONGO_URI'])
db = client.health_monitoring
health_data_collection = db.health_data

@health_data_bp.route('/api/health-data', methods=['GET', 'POST'])
def health_data():
    if request.method == 'GET':
        data = list(health_data_collection.find())
        return jsonify(data)
    if request.method == 'POST':
        new_data = request.json
        health_data_collection.insert_one(new_data)
        return jsonify({'message': 'Data added successfully'})
