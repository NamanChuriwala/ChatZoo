from app import create_app
from flask_socketio import SocketIO, emit
from flask_socketio import join_room, leave_room

app = create_app()
socketio = SocketIO(app)

@socketio.on("message to server")
def send_message(data):
    response = {}
    response['message'] = data['message']
    response['user'] = data['username']
    emit('display message', response, broadcast=True)

@socketio.on('join')
def join(data):
    join_room(data['room'])
    response = {}
    response['message'] = data['username'] + ' has joined the chat'
    emit('display message', response, room=data['room'])

@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    response = {}
    response['message'] = data['username'] + ' has left the chat ' + data['room']
    emit('display message', response, room=data['room'])

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
