from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    socketio.send(data)  # Broadcast the received message to all clients

@socketio.on('connect')
def handle_connect():
    # Optional: Can be used for other connection messages if needed
    pass

if __name__ == '__main__':
    socketio.run(app)
