import { Component, OnInit } from '@angular/core';
import { SocketService } from '../socket.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
	inRoom: boolean;
	messages = [];
	connection;
	message;
  constructor(private socketService: SocketService) {
  	this.inRoom = false;
  }

  ngOnInit() {
    // this.connection = this.socketService.getMessages().subscribe(message => {
    //   this.messages.push(message);
    // });
    this.socketService.hello();
    this.socketService.sendMessage("Connecting to rum now");
  }


  sendMessage(){
    this.socketService.sendMessage(this.message);
    this.message = '';
  }

  ngOnDestroy() {
    this.connection.unsubscribe();
  }

}
