import socket

HOST = '127.0.0.1'
PORT = 4000

while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print("Client connected")
        break
    except:
        print("Server offline")

while True:
    msg = input("Your message: ")
    client.send(msg.encode())
    print("Message sent")
    if msg == "exit":
        break
    data = client.recv(1024)
    print("Server answered: ", data.decode())

client.close()
print("Client closed")