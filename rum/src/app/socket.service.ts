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
	hello(): void {
		console.log("Hello from socket service!");
	}
  constructor() {
  	this.messages = [];
  	this.socket = io.connect(this.url);
  	this.socket.on("connect",(data) => console.log("This is only a test"));
  	this.socket.on('json_message', (data) => {
  	  this.previousSessionMessages = data.messages;
  	});
  	this.socket.on('simple_message',(data) => {
  			this.messages.push(data);
  	});
  }

  getMessages(){
  	return this.messages;
  }
  // getSessionMessages(){
  // 	return this.previousSessionMessages;
  // }

  sendMessage(message){
      this.socket.emit('add-message', message);
  }

}
