from flask import Flask, request, jsonify
from pymongo import MongoClient
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np
from twilio.rest import Client

app = Flask(__name__)

# MongoDB setup
client = MongoClient('localhost', 27017)
db = client.health_monitoring
health_data_collection = db.health_data

# Twilio setup
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_client = Client(account_sid, auth_token)

# Example LSTM model setup (assume pre-trained model is saved)
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(10, 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

@app.route('/api/health-data', methods=['GET', 'POST'])
def health_data():
    if request.method == 'GET':
        # Logic to return historical health data
        data = list(health_data_collection.find())
        return jsonify(data)
    if request.method == 'POST':
        # Logic to submit new health data
        new_data = request.json
        health_data_collection.insert_one(new_data)
        return jsonify({'message': 'Data added successfully'})

@app.route('/api/predict', methods=['POST'])
def predict():
    # Logic to return predictive alerts
    data = request.json
    features = np.array(data['features']).reshape(-1, 10, 1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/api/user', methods=['GET'])
def user():
    # Logic to return user information
    user_info = {'name': 'John Doe', 'age': 30}
    return jsonify(user_info)

@app.route('/api/notify', methods=['POST'])
def notify():
    # Logic to send SMS notification
    to_number = request.json.get('to')
    message_body = request.json.get('body')
    message = twilio_client.messages.create(
        body=message_body,
        from_='+1234567890',
        to=to_number
    )
    return jsonify({'message': 'Notification sent successfully'})

if __name__ == '__main__':
    app.run(debug=True)

