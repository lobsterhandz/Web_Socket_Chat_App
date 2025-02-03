from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

# Initialize Flask App
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Hashmap storage for messages (Key = Username, Value = List of Messages)
message_storage = {}

@app.route("/")
def index():
    return render_template("websocket_client.html")  # Frontend WebSocket Client

# WebSocket Event Handlers
@socketio.on("connect")
def handle_connect():
    print("🔗 Client Connected!")

@socketio.on("disconnect")
def handle_disconnect():
    print("❌ Client Disconnected!")

@socketio.on("send_message")
def handle_message(data):
    """Stores messages in a Hashmap (User -> List of Messages)"""
    user = data.get("user")
    message = data.get("message")

    if not user or not message:
        return emit("error", {"error": "User and message required!"}, broadcast=False)

    if user not in message_storage:
        message_storage[user] = []

    message_storage[user].append(message)
    print(f"📩 Message from {user}: {message}")

    emit("message_received", {"user": user, "message": message}, broadcast=True)

@socketio.on("get_all_messages")
def get_all_messages(data):
    """Retrieves all messages sent by a specific user"""
    user = data.get("user")

    if user in message_storage:
        messages = message_storage[user]
    else:
        messages = []

    emit("message_history", {"user": user, "messages": messages}, broadcast=False)

if __name__ == "__main__":
    print("✅ WebSocket Server Running on http://127.0.0.1:5000/")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
