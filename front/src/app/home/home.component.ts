import {
  Component,
  OnInit
} from '@angular/core';
import { Subscription } from 'rxjs/Subscription';

import { AppState } from '../app.service';
import { Title } from './title';
import { XLargeDirective } from './x-large';
import { SocketService } from '../services/socket.service'

@Component({
  /**
   * The selector is what angular internally uses
   * for `document.querySelectorAll(selector)` in our index.html
   * where, in this case, selector is the string 'home'.
   */
  selector: 'home',  // <home></home>
  /**
   * We need to tell Angular's Dependency Injection which providers are in our app.
   */
  providers: [
    Title,
    SocketService
  ],
  /**
   * Our list of styles in our component. We may add more to compose many styles together.
   */
  styleUrls: [ './home.component.css' ],
  /**
   * Every Angular template is first compiled by the browser before Angular runs it's compiler.
   */
  templateUrl: './home.component.html'
})


export class HomeComponent implements OnInit {
  public message: any;
  public subscription: Subscription;

  /**
   * Set our default values 
   */
  public localState = { value: '' };
  /**
   * TypeScript public modifiers
   */
  constructor(
    public appState: AppState,
    public title: Title,
    private socketService: SocketService
  ) {
    this.subscription = this.socketService.getMessage().subscribe(message => {
      this.message = message;
      alert(this.message.text);
    });
  }

  public ngOnInit() {
    this.socketService.helloWorld();
  }

  public ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}
