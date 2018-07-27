import { Component } from '@angular/core';
import { CardComponent } from './card/card.component'
// import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'rum';

  // constructor(private domSanitizer: DomSanitizer,private cardComponent: CardComponent) {
  // 	// this.cardComponent = this.domSanitizer.bypassSecurityTrustHtml('svg');
  // }
}
