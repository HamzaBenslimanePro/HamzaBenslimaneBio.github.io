from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/user', methods=['GET'])
def user():
    user_info = {'name': 'John Doe', 'age': 30}
    return jsonify(user_info)
