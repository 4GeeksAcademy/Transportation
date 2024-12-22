from flask import Flask, jsonify
from flask_cors import CORS
from api.models import db
from api.routes import api
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure CORS to allow requests from frontend
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Register blueprint
app.register_blueprint(api, url_prefix='/api')

# Root route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Transportation API"}), 200

# Create tables
with app.app_context():
    try:
        db.create_all()
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {str(e)}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3001, debug=True)
