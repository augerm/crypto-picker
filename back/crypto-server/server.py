import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
























# -----------------------------------------------------------------------


# import asyncio
# from websocket_server import WebsocketServer

# PORT=9002
# server = WebsocketServer(PORT)

# # Called for every client connecting (after handshake)
# @asyncio.coroutine
# def new_client(client, server):
# 	print("New client connected and was given id %d" % client['id'])
# 	server.send_message_to_all("Hey all, a new client has joined us")

# # Called for every client disconnecting
# @asyncio.coroutine
# def client_left(client, server):
# 	print("Client(%d) disconnected" % client['id'])

# # Called when a client sends a message
# @asyncio.coroutine
# def message_received(client, server, message):
# 	if len(message) > 200:
# 		message = message[:200]+'..'
# 	print("Client(%d) said: %s" % (client['id'], message))

# # Send message to client
# @asyncio.coroutine
# def send_message_to_client(msg):
# 	server.send_message_to_all("NEW MESSAGE")

# @asyncio.coroutine
# def start_server(): 
# 	server.set_fn_new_client(new_client)
# 	server.set_fn_client_left(client_left)
# 	server.set_fn_message_received(message_received)
# 	server.run_forever()

# start_server()