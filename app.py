from flask import Flask
from flask_cors import CORS
from api.models import db
from api.routes import api
import os
from dotenv import load_dotenv
import pyodbc
from sqlalchemy import event
from sqlalchemy.engine import Engine

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration with detailed error handling
try:
    # Print the connection string for debugging (remove sensitive info first)
    connection_string = os.getenv('DATABASE_URL')
    print(f"Attempting to connect with: {connection_string.split('@')[1]}")  # Only print server/database part
    
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_timeout': 30,
        'pool_recycle': 1800,
        'pool_pre_ping': True,
        'connect_args': {
            'connect_timeout': 30
        }
    }
    
    db.init_app(app)
    
    # Test the connection explicitly
    with app.app_context():
        try:
            db.engine.connect()
            print("Test connection successful!")
            db.create_all()
            print("Database tables created successfully!")
        except Exception as e:
            print(f"Test connection failed: {str(e)}")
            raise

except Exception as e:
    print(f"Database configuration error: {str(e)}")
    raise

@event.listens_for(Engine, "connect")
def set_connection_timeout(dbapi_connection, connection_record):
    try:
        dbapi_connection.timeout = 30
    except Exception as e:
        print(f"Could not set timeout: {str(e)}")

app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True) 