import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server_socket = None
        self.client_socket = None
        self.max_message_size = 1024

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def accept_client(self):
        self.client_socket, _addr = self.server_socket.accept()

    def disconnect_client(self):
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None

    def stop(self):
        self.disconnect_client()
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None

    def send(self, text):
        self.client_socket.send(text.encode())

    def receive(self):
        data = self.client_socket.recv(self.max_message_size)
        return data.decode()
