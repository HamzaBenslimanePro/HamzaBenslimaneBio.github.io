from flask import Blueprint, request, jsonify
import numpy as np
from models.load_model import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

predict_bp = Blueprint('predict', __name__)

# Load the pre-trained model
model = load_model('models/model.pkl')

@predict_bp.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(-1, 10, 1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})
