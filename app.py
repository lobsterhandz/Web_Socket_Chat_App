from flask import render_template, request
from flask_socketio import join_room, leave_room, emit
from web_socket_server import create_app, socketio

# Create Flask app instance
app = create_app()

# Hashmap storage for messages (Key = Room, Value = List of Messages)
message_storage = {}

# Preset Room List
preset_rooms = {"general", "gaming", "movies", "tech", "random"}

@app.route("/")
def index():
    return render_template("index.html")  # Username entry page

@app.route("/join_room")
def join_room_page():
    return render_template("join_room.html")  # Room selection page

@app.route("/chat")
def chat():
    username = request.args.get("username")
    room = request.args.get("room")
    if not username or not room:
        return "Invalid room or username", 400
    return render_template("chat.html", username=username, room=room, rooms=preset_rooms)

# WebSocket Event Handlers
@socketio.on("connect")
def handle_connect():
    print("🔗 Client Connected!")

@socketio.on("disconnect")
def handle_disconnect():
    print("❌ Client Disconnected!")

@socketio.on("join_room")
def handle_join(data):
    """Handles a user joining a room."""
    username = data.get("username")
    room = data.get("room")
    
    if not username or not room:
        return emit("error", {"error": "Username and room required!"}, broadcast=False)
    
    if room not in preset_rooms:
        return emit("error", {"error": "Invalid room!"}, broadcast=False)
    
    join_room(room)
    print(f"🚪 {username} joined {room}")
    
    if room not in message_storage:
        message_storage[room] = []
    
    emit("room_message", {"user": "System", "message": f"{username} has joined {room}"}, room=room)
    emit("update_rooms", list(preset_rooms), broadcast=True)  # Ensure all users get the room list

@socketio.on("leave_room")
def handle_leave(data):
    """Handles a user leaving a room."""
    username = data.get("username")
    room = data.get("room")
    
    if not username or not room:
        return emit("error", {"error": "Username and room required!"}, broadcast=False)
    
    leave_room(room)
    print(f"🚪 {username} left {room}")
    
    emit("room_message", {"user": "System", "message": f"{username} has left {room}"}, room=room)
    emit("update_rooms", list(preset_rooms), broadcast=True)

@socketio.on("send_message")
def handle_message(data):
    """Stores messages per room and broadcasts within the room."""
    username = data.get("username")
    room = data.get("room")
    message = data.get("message")
    
    if not username or not message or not room:
        return emit("error", {"error": "Username, room, and message required!"}, broadcast=False)
    
    if room not in message_storage:
        message_storage[room] = []
    
    message_storage[room].append({"user": username, "message": message})
    print(f"📩 {username} in {room}: {message}")
    
    emit("room_message", {"user": username, "message": message}, room=room)

@socketio.on("get_room_messages")
def get_room_messages(data):
    """Retrieves all messages from a specific room."""
    room = data.get("room")
    messages = message_storage.get(room, [])
    emit("room_history", {"room": room, "messages": messages}, broadcast=False)

@socketio.on("get_rooms")
def get_rooms():
    """Send the list of preset rooms."""
    emit("update_rooms", list(preset_rooms), broadcast=False)

if __name__ == "__main__":
    print("✅ WebSocket Server Running on http://127.0.0.1:5000/")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)