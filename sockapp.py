from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, \
	close_room, rooms, disconnect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return "Hello from flask app!"

@socketio.on('add-message')
def test_message(message):
	print(message)
	emit('custom_message', {'message':f"Bounced back from server: \"{message}\"",'room':0})

@socketio.on('connect')
def test_connect():
	join_room(0)
	emit('custom_message', {'message':'Congratulations! You are connected','room':0})

@socketio.on('disconnect')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	socketio.run(app,debug=True)
