import { Injectable } from '@angular/core';


import { Subject } from 'rxjs/Subject';
import { Observable } from 'rxjs/Observable';
import * as io from 'socket.io-client';

@Injectable()
export class SocketService {

	private url = 'http://localhost:5000';

	private socket;

	hello(): void {
		console.log("Hello from socket service!");
	}
  constructor() {
  	this.socket = io.connect(this.url);
  	this.socket.on("connection",(data) => console.log("This is only a test"));
  	this.socket.on('custom_message', (data) => {
  		console.log("Received a message!");
  	  console.log(data);
  	  console.log(data.message);
  	});
  }


  sendMessage(message){
      this.socket.emit('add-message', message);
  }

}
