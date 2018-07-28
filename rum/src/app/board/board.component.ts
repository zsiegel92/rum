import { Component, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
	inRoom: boolean;
	messages;
	connection;
	message;
	url2 = window.location.href.split(":",2).join(":") + ":5000";
	url3 = location.protocol + '//' + document.domain + ':' + 5000;
  constructor(private socketService: SocketService) {
  	this.inRoom = false;

  }

  ngOnInit() {
    // this.connection = this.socketService.getMessages().subscribe(message => {
    //   this.messages.push(message);
    // });
    this.socketService.hello();
    this.socketService.sendMessage("Connecting to rum now");
    this.messages=this.socketService.messages;
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

  ngOnDestroy() {
    this.connection.unsubscribe();
  }

}
