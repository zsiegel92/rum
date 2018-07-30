import { Injectable } from '@angular/core';


import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';
import * as io from 'socket.io-client';

@Injectable()
export class SocketService {

	// private url = 'http://localhost:5000'
	// private url = window.location.href.split(":",2).join(":") + ":5000";
	private url = location.protocol + '//' + document.domain + ':' + 5000;


	private socket;
	public messages;
	public previousSessionMessages;
	public rooms;
	public users;
	public available_rooms;
	private username;
	hello(): void {
		console.log("Hello from socket service!");
	}
  constructor() {
  	this.messages = [];
  	this.rooms=[];
  	this.users=[];
  	this.socket = io.connect(this.url);
  	this.socket.on("connect",(data) => console.log("This is only a test"));
  	this.socket.on('json_message', (data) => {
  	  this.previousSessionMessages = data.messages;
  	});
  	this.socket.on('simple_message',(data) => {
	  		console.log("Received a simple message: '" + data + "'");
  			this.messages.push(data);
  	});

  	this.socket.on('roll-call',(data) => {
  		console.log("Roll call requested! Emitting 'present'");
  		this.socket.emit('present',{'rooms':this.rooms,'users':this.users});
  	});

  	this.socket.on('state-announcement',(data) => {


  		for (let room of data.rooms){
  			if (!this.roomExists(room.name)){
  				this.rooms.push(room);
  			}
  			else {
  				let the_room = this.getRoomByName(room.name);
  				for (let user of room.users){
  					if (!the_room.users.includes(user)){
  						the_room.users.push(user);
  					}
  				}

  			}
  		}

  		for (let user of data.users){
  			if (!this.users.includes(user)){
  				this.users.push(user);
  			}
  		}
  	});

  	this.socket.on('client-disconnect',(data)=> {
  		console.log("a client disconnected");
  		//remove from users
  	});

  	this.getRooms();
  }

  getRoomByName(room_name){
  	for (let a_room of this.rooms){
  		if (a_room.name == room_name){
  			return a_room;
  		}
  	}
  }
  getRooms() {
  	this.socket.emit('get-rooms');
  }

  createRoom(room_name){
  	if (this.roomExists(room_name)){
  		alert("Room " + room_name + " already exists.");
  	}
  	else {
  		console.log("Attempting to create '" + room_name + "'.");
  		this.rooms.push({'name':room_name,'owner':this.username,'users':[this.username]});
  		this.socket.emit('create-room',room_name);
  	}
  }
  getMessages(){
  	return this.messages;
  }
  joinRoom(room_name){
  	this.socket.emit('join-room',room_name);
  }
  roomExists(room_name){
  	let room_exists=false;
  	for (let room of this.rooms){
  		if (room.name==room_name){
  			room_exists=true;
  		}
  	}
  	return room_exists;
  }
  // getSessionMessages(){
  // 	return this.previousSessionMessages;
  // }

  sendMessage(message){
      this.socket.emit('add-message', message);
  }
  setUsername(user_name){
  	if (this.users.includes(user_name)){
  		alert("User Name '" + user_name + "' already exists!");
  	}
  	else{
  		this.username=user_name;
  		this.users.push(this.username);
  		this.socket.emit('set-username',user_name);
  	}
  }

  getUsername(){
  	return this.username;
  }

}
