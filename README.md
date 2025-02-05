# WebSocket Chat Application

## 📌 Overview
This is a real-time chat application powered by **Flask**, **Socket.IO**, and a simple frontend using **HTML, CSS, and JavaScript**. It enables users to send and receive messages instantly using WebSockets.
# WebSocket Chat App - CI/CD with GitHub Actions
To ensure the reliability of the project, we have implemented a CI/CD pipeline using GitHub Actions. The pipeline automates testing before merging changes into the main branch.

## Features
## 🚀 Features
- **Username-based chat** (users can input their name before sending messages).
- **Live message updates** (new messages appear instantly).
- **Lightweight frontend** (pure HTML, CSS, and vanilla JavaScript).
<<<<<<< Updated upstream
<<<<<<< Updated upstream
# WebSocket Chat Application

=======
- **WebSocket Communication**: Real-time messaging using Flask-SocketIO.
- **Chat Rooms**: Users can join different rooms and send messages.
- **Text Effects & Emojis**: Users can format messages and use emojis.
- **CI/CD Pipeline**: Automated testing and validation before deployment.

=======
- **WebSocket Communication**: Real-time messaging using Flask-SocketIO.
- **Chat Rooms**: Users can join different rooms and send messages.
- **Text Effects & Emojis**: Users can format messages and use emojis.
- **CI/CD Pipeline**: Automated testing and validation before deployment.

>>>>>>> Stashed changes
## Running the Project
### **1. Installation**
Ensure you have Python and dependencies installed:
```sh
pip install -r requirements.txt
```

### **2. Starting the WebSocket Server**
Run the server:
```sh
python app.py
```
Access the chat at:
```
http://127.0.0.1:5000/
```

### **3. Running Tests Locally**
To verify the integrity of the helper functions, run:
```sh
python -m unittest discover -s . -p "test_utils.py"
```

## CI/CD Pipeline (GitHub Actions)
### **Workflow Process**
- **Feature Branch (`feature/tests`)**: Runs automated tests before merging into `main`.
- **Tests Included:**
  - `sum_numbers()` (validates positive & negative sums)
  - `is_palindrome()` (checks for palindromes)
  - `factorial()` (ensures correct factorial calculation & raises errors on negatives)
  - `is_even()` (checks if a number is even)

### **Workflow Configuration (`.github/workflows/main.yml`)**
The CI/CD pipeline is triggered on:
- **Push to `feature/tests` branch**
- **Pull requests to `main` branch**

### **Running Tests in CI/CD**
1. GitHub automatically runs the tests when pushing changes to `feature/tests`.
2. If all tests pass, the branch is safe to merge into `main`.
3. If tests fail, the workflow prevents broken code from being deployed.

### **Deployment**
Once merged into `main`, the application can be deployed manually or via automated deployment steps added to the pipeline.

## Contributing
1. **Fork the repository**.
2. **Create a feature branch** (`feature/new-feature`).
3. **Commit and push changes**.
4. **Create a pull request (PR)**.
5. **Ensure tests pass before merging**.

## Future Enhancements
- **User Authentication**: Implement user accounts & authentication.
- **Database Integration**: Store chat messages persistently.
- **UI Improvements**: Enhance frontend UI with React.


# WebSocket Chat Application

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
<<<<<<< Updated upstream

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
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

## 👤 Project Structure
```
/websocket-chat-app
│── /templates
│   └── websocket_client.html  # Frontend client for testing chat
│── app.py                     # Main Flask app with WebSocket routes
│── web_socket_server.py        # WebSocket server setup
│── requirements.txt            # Dependencies for the project
│── README.md                   # Project documentation
│── utils.py                    # Collection Utility functions
│── test_utils.py               # Test for integration of utils
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
## 🛠️ Technologies Used
- **Backend**: Flask, Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **WebSockets**: Socket.IO
- **Tools**: Postman (for WebSocket testing)

---

