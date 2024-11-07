# src/flask_api_example/app.py
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/api/greet/<name>', methods=['GET'])
    def greet(name):
        return jsonify(message=f"Hello, {name}!")

    return app

def main():
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
