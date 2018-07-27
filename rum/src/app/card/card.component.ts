import { Component, OnInit, Input, ApplicationRef, Pipe,PipeTransform  } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';


@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
	@Input() single: string;
	@Input() double1: string;
	@Input() double2: string;


  constructor(private ref: ApplicationRef) {
  	this.single="blue";
  	this.double1="red";
  	this.double2="green";
  	// this.ref.tick();
  	// this.svgTemplate = this.domSanitizer.bypassSecurityTrustHtml(svg);
  }

  ngOnInit() {

  }

}
