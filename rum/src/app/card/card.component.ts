import { Component, OnInit, Input  } from '@angular/core';



@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
	@Input() single: string;
	@Input() double1: string;
	@Input() double2: string;


  constructor() {
  	this.single="blue";
  	this.double1="red";
  	this.double2="green";
  }

  ngOnInit() {

  }

}
