from Server.Model.model_server import Server

HOST = '127.0.0.1'
PORT = 4000


server = Server(HOST, PORT)
server.start()
server.accept_client()

while True:
    msg=server.receive()
    print("Client say: ", msg)

    if msg == "exit":
        break

    result=input("Server say: ")
    server.send(result)

server.stop()