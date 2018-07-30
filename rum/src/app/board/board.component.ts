import { Component, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
	messages;
	connection;
	message;
	rooms;
	users;
	room_name;
	username;
	usernameSet=false;
	url2 = window.location.href.split(":",2).join(":") + ":5000";
	url3 = location.protocol + '//' + document.domain + ':' + 5000;



  constructor(private socketService: SocketService) {

  }

  ngOnInit() {
    // this.connection = this.socketService.getMessages().subscribe(message => {
    //   this.messages.push(message);
    // });
    this.socketService.hello();
    // this.socketService.sendMessage("Connecting to rum now");
    this.messages=this.socketService.messages;
    this.rooms = this.socketService.rooms;
    this.users = this.socketService.users;
  }

  sendMany(){
  	for (let i = 0; i < 100; i++) {
	  	this.sendMessage("Testing " + i);
  	}
  }
  sendMessage(message){
    this.socketService.sendMessage(message);
    this.message = '';
  }
  createRoom(room_name){
  	this.socketService.createRoom(room_name);
  	this.room_name = '';
  }

  joinRoom(room_name){
  	this.socketService.joinRoom(room_name);
  }
  ngOnDestroy() {
    this.connection.unsubscribe();
  }

  setUsername(user_name){
  	this.socketService.setUsername(user_name);
  	this.username = this.socketService.getUsername();
  	this.usernameSet=true;
  }

}
