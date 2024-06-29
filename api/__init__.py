from flask import Flask
from api.health_data import health_data_bp
from api.predict import predict_bp
from api.user import user_bp
from api.notify import notify_bp

app = Flask(__name__)

# Register blueprints for API endpoints
app.register_blueprint(health_data_bp, url_prefix='/api/health-data')
app.register_blueprint(predict_bp, url_prefix='/api/predict')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(notify_bp, url_prefix='/api/notify')

if __name__ == '__main__':
    app.run(debug=True)
