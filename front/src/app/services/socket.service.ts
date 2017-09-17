import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Subject } from 'rxjs/Subject';

@Injectable()
export class SocketService {
	public sentimentSocket: any;
	private subject = new Subject<any>();

	constructor() {
		this.sentimentSocket = new WebSocket("ws://localhost:8888");
		this.sentimentSocket.onopen = (event) => {
			this.sentimentSocket.send("Here's some text that the server is urgently awaiting!"); 
			this.sentimentSocket.onmessage = (msg) => {
				this.sendMessage(msg.data);
			};
		};
	}

	public helloWorld(): void {
		console.log("Hello World");
	}

	public sendMessage(message: string) {
		this.subject.next({ text: message });
	}

	public clearMessage() {
		this.subject.next();
	}

	public getMessage(): Observable<any> {
		return this.subject.asObservable();
	}
}