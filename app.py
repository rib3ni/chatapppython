from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    # 'data' will be a dictionary containing 'user' and 'msg'
    print(f"Message from {data['user']}: {data['msg']}")
    send(data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
