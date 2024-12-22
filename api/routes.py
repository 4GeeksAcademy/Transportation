from flask import Blueprint, jsonify
from .models import db, Product
import os
import pyodbc

api = Blueprint('api', __name__)

# Test route to verify API is working
@api.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API"}), 200

# Products route
@api.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([product.serialize() for product in products]), 200
    except Exception as e:
        print(f"Error in get_products: {str(e)}")  # Debug print
        return jsonify({"error": str(e)}), 500

# Add test data route
@api.route('/add-test-product', methods=['GET'])
def add_test_product():
    try:
        # Create a test product
        test_product = Product(
            name="Test Product",
            description="This is a test product",
            price=99.99
        )
        db.session.add(test_product)
        db.session.commit()
        return jsonify({"message": "Test product added successfully"}), 200
    except Exception as e:
        print(f"Error adding test product: {str(e)}")  # Debug print
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Hello route for testing
@api.route('/hello', methods=['GET'])
def handle_hello():
    return jsonify({"message": "Hello from the API!"}), 200