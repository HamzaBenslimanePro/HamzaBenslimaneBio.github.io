from flask import Blueprint, request, jsonify
from twilio.rest import Client

notify_bp = Blueprint('notify', __name__)

# Twilio setup
twilio_client = Client(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])

@notify_bp.route('/api/notify', methods=['POST'])
def notify():
    to_number = request.json.get('to')
    message_body = request.json.get('body')
    message = twilio_client.messages.create(
        body=message_body,
        from_='+1234567890',
        to=to_number
    )
    return jsonify({'message': 'Notification sent successfully'})
