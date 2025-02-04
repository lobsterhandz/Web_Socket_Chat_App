from flask import Flask
from flask_socketio import SocketIO

# Initialize SocketIO globally
socketio = SocketIO()

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecretkey"  # Optional for session security

    # Initialize WebSocket with CORS support
    socketio.init_app(app, cors_allowed_origins="*")

    return app
