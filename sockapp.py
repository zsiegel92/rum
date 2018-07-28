from flask import Flask, render_template,session,request,redirect
from flask_socketio import SocketIO, emit, join_room, leave_room, \
	close_room, rooms, disconnect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
	return redirect(":".join(request.url_root.split(":")[:2])+":4200")

@socketio.on('add-message')
def test_message(message):
	print(message)
	# print(f"All the rooms are: {socketio.rooms['/'].keys()}")
	if session.get('messages'):
		session['messages'].append(message)
	else:
		session['messages']=[message]
	print(session['messages'])
	emit('json_message', {'message':f"Session messages are: '{session.get('messages')}'",'messages':session.get('messages'),'room':rooms()[0]},room=rooms()[0])
	emit('simple_message',message,room=rooms()[0])

@socketio.on('connect')
def test_connect():
	# join_room(0)
	print(f"Rooms are: {rooms()}")
	emit('json_message', {'message':'Congratulations! You are connected','room':0})

@socketio.on('disconnect')
def disconnecter():
	for room in rooms():
		leave_room(room)
	print('Client disconnected')

@socketio.on('connect')
def connecter():
	emit('simple_message',"You are connected!",room=rooms()[0])

if __name__ == '__main__':
	socketio.run(app,debug=True,host='0.0.0.0')
