from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Handle incoming messages
@socketio.on('message')
def handle_message(data):
    # data will be a dictionary containing 'user' and 'msg'
    print(f"Message from {data['user']}: {data['msg']}")
    send(data, broadcast=True)  # Broadcast message to all users
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
