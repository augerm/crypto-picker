import time
import threading
import logging
from queue import Queue


class twitterThread (threading.Thread):
   def __init__(self, threadID, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.q = q
   def run(self):
      # import twitter
      counter = 0
      while(True):
        counter += 1
        self.q.put("Item " + str(counter))
        time.sleep(1)


class clientThread (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        while(True):
            print(self.q.get())
            time.sleep(3)
        # from websocket_server import WebsocketServer
        # server = WebsocketServer(8888, host='http://localhost')
        # server.set_fn_new_client(new_client)
        # server.run_forever()

q = Queue()
thread1 = twitterThread(1, q)
thread2 = clientThread(2, q)
thread1.start()
thread2.start()






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