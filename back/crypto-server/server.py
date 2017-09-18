import time
import threading
import logging
from queue import Queue

from twitter import Twitter
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class twitterThread (threading.Thread):
   def __init__(self, threadID, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.q = q
   def run(self):
      twitter = Twitter(self.q)


clients = []
class SimpleSocket(WebSocket):
    def __init__(self, q):
        self.q = q
        while(True):
            try: 
                for items in range(0, self.q.qsize()):
                    item = self.q.get_nowait()
                    print(item)
                    for client in clients:
                        client.sendMessage(item)
                time.sleep(3)
            except Queue.Empty:
                pass

    def handleConnected(self):
       print("Client joined")
       clients.append(self)

    def handleClose(self):
       print("Client Left")
       clients.remove(self)

q = Queue()
thread1 = twitterThread(1, q)
thread1.start()

server = SimpleWebSocketServer('', 8888, SimpleSocket(q))
server.serveforever()




# ----------------------------------------------------------------------------------------------------------------------

# class clientThread (threading.Thread):
#   def __init__(self, threadID):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#   def run(self):
#       import asyncio
#       import websockets
#       from pyee import EventEmitter
#       ee = EventEmitter()
#       @ee.on('sentiment-update')
#       async def onMessage(msg):
#           print("Received message")
#           websocket.send(msg)

#       async def hello(websocket, path):
#           name = await websocket.recv()
#           print("Received Message")

#           greeting = ("Hello World")
#           await websocket.send(greeting)
#           print("Sent message")

#       start_server = websockets.serve(hello, 'localhost', 8888)

#       asyncio.get_event_loop().run_until_complete(start_server)
#       while(True):
#           asyncio.get_event_loop()
#           ee.emit("sentiment-update")
#           time.sleep(1)   