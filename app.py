from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Process the message payload
    if request.method == 'GET':
        # Handle GET request
        # client.publish("testingProjectBGU", payload="FlaskGET", qos=0, retain=False)
        print("In GET request")
        return 'This is a GET request', 200
    elif request.method == 'POST':
        # Handle POST request
        # client.publish("testingProjectBGU", payload="FlaskPOST", qos=0, retain=False)
        print("In POST request")
        socketio.emit('server_message', 'Message received from Salesforce!')
        return 'This is a POST request', 200

if __name__ == '__main__':
    socketio.run(app)