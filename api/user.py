from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_user_info():
    # Logic to return user information
    user_info = {'name': 'John Doe', 'age': 30}
    return jsonify(user_info)
