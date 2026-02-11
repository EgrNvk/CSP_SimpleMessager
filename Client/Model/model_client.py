import socket
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.is_connected = False
        self.max_message_size = 1024

    def connect(self):
        while True:
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect((self.host, self.port))
                self.is_connected = True
                print("Connected to server")
                break

            except:
                print("Server offline")
                time.sleep(5)

    def disconnect(self):
        if self.socket:
            self.socket.close()
        self.is_connected = False

    def send(self, text):
        self.socket.send(text.encode())

    def receive(self):
        data = self.socket.recv(self.max_message_size)
        return data.decode()

    def get_status(self):
        return self.is_connected