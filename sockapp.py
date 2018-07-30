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

# @socketio.on('connect')
# def test_connect():
# 	join_room("lobby")
# 	print(f"Rooms are: {rooms()}")
# 	emit('json_message', {'message':'Congratulations! You are connected','room':0})


@socketio.on('get-rooms')
def get_rooms():
	emit('roll-call',room='lobby')


@socketio.on('create-room')
def room_creator(room_name):
	# print("User " + request.sid + " attempting to join room " + room_name)
	join_room(room_name)
	# print(f"rooms(): {rooms()}")
	emit('roll-call',room='lobby')
@socketio.on('join-room')
def room_joiner(room_name):
	join_room(room_name)
	emit('roll-call',room='lobby')

@socketio.on('set-username')
def set_username(user_name):
	session['username']=user_name
	emit('roll-call',room='lobby')

@socketio.on('present')
def announce_state(json):
	print(json)
	session['users']=json['users']
	session['rooms']=json['rooms']
	# the_rooms = []
	# for i,room in enumerate(rooms()):
	# 	if (room==request.sid) or (room=='lobby'):
	# 		the_rooms.append(room)
	the_rooms = [room for room in rooms() if (room != 'lobby') and (room != request.sid)]

	stateful_rooms = []
	room_exists=False
	for room in the_rooms:
		for i,a_stateful_room in enumerate(session['rooms']):
			if a_stateful_room['name']==room:
				the_stateful_room=a_stateful_room
				room_exists=True
		if room_exists:
			room_users = the_stateful_room['users']
			if session['username'] not in room_users:
				room_users.append(session['username'])
			stateful_rooms.append({'name':room,'owner':the_stateful_room['owner'],'users':room_users})
	emit('state-announcement',{'rooms':stateful_rooms,'users':json['users']},room='lobby')

@socketio.on('disconnect')
def disconnecter():
	emit("client-disconnect")
	for room in rooms():
		leave_room(room)
	print('Client disconnected')

@socketio.on('connect')
def connecter():
	join_room("lobby")
	emit('simple_message',"You are connected!",room=rooms()[0])

if __name__ == '__main__':
	socketio.run(app,debug=True,host='0.0.0.0')
