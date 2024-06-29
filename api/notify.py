from flask import Blueprint, jsonify
from twilio.rest import Client

notify_bp = Blueprint('notify', __name__)

# Twilio setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)

@notify_bp.route('/', methods=['POST'])
def send_notification():
    # Logic to send SMS notification
    to_number = request.json.get('to')
    message_body = request.json.get('body')
    message = twilio_client.messages.create(
        body=message_body,
        from_='+1234567890',
        to=to_number
    )
    return jsonify({'message': 'Notification sent successfully'})
