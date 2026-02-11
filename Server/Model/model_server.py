import socket

HOST = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server start")
conn, addr = server.accept()
print("Client connected by", addr)
while True:
    data = conn.recv(1024)
    msg = data.decode()
    print("Client say: ", msg)

    if msg == "exit":
        break

    result = input("You say: ")
    conn.send(str(result).encode())
    # print("Client sent", result)

conn.close()
server.close()
print("Server closed")