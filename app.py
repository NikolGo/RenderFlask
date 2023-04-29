from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Process the message payload
    print("In POST request")
    data = request.get_json()
    # message = data['Location Id']
    print(data)
    socketio.emit('occupancy_update', data)
    return 'This is a POST request', 200

if __name__ == '__main__':
    socketio.run(app)
