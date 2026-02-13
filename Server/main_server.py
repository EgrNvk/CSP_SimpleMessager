from Server.Model.model_server import Server
from Server.View.view_server import ServerView
from Server.Controller.controller_server import ServerController

HOST = '127.0.0.1'
PORT = 4000

view = ServerView(title="Server")
server = Server(HOST, PORT)

controller = ServerController(view, server)
controller.start()

view.start()