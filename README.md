# WebSocket Chat Application

## 📌 Overview
This is a real-time chat application powered by **Flask**, **Socket.IO**, and a simple frontend using **HTML, CSS, and JavaScript**. It enables users to send and receive messages instantly using WebSockets.

## 🚀 Features
- **Real-time messaging** with WebSockets.
- **Username-based chat** (users can input their name before sending messages).
- **Live message updates** (new messages appear instantly).
- **Lightweight frontend** (pure HTML, CSS, and vanilla JavaScript).
# WebSocket Chat Application

## NEW Features

### Rooms
- Users can join predefined rooms: General Chat, Gaming Talk, Movie Discussion, Tech Enthusiasts, and Random Fun.
- The room selection dropdown ensures users can switch between any of the predefined rooms at any time.
- Users receive real-time updates when others join or leave a room.

### Emojis
- A clickable emoji panel allows users to insert emojis into their messages effortlessly.
- The emoji selection enhances chat interactions, making conversations more engaging and expressive.

### Text Effects
- Users can customize their messages with text effects like bold, italic, and color changes.
- A simple dropdown menu enables users to apply styles to their text before sending messages.

## Setup & Installation
(Include your existing setup instructions here)

## Usage
(Include your existing usage instructions here)

## License
(Include license details here)
## 🛠️ Technologies Used
- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **WebSockets**: Socket.IO
- **Tools**: Postman (for WebSocket testing)

## 👤 Project Structure
```
/websocket-chat-app
│── /templates
│   └── websocket_client.html  # Frontend client for testing chat
│── app.py                     # Main Flask app with WebSocket routes
│── web_socket_server.py        # WebSocket server setup
│── requirements.txt            # Dependencies for the project
│── README.md                   # Project documentation
```

## ⚡ Installation & Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/websocket-chat-app.git
   cd websocket-chat-app
   ```

2. **Create a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```sh
   python app.py
   ```

5. **Access the chat UI**  
   Open a browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## 📡 WebSocket Testing (Using Postman)
To test WebSocket connections in **Postman**:

1. Open **Postman** and go to **New > WebSocket Request**
2. Set the WebSocket URL to:
   ```
   ws://127.0.0.1:5000/socket.io/
   ```
3. Add an **event listener** for `get_all_messages`
4. Send a message using the following JSON format:
   ```json
   {
      "user": "JohnDoe",
      "message": "Hello world!"
   }
   ```
5. Observe the real-time message updates.

## 🔧 Future Enhancements
- Add a user authentication system.
- Store chat history in a database.
- Improve the frontend UI with a modern framework like React.

## ✨ License
This project is open-source and available under the **MIT License**.

---

