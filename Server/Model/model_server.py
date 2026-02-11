import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.conn = None
        self.addr = None
        self.max_message_size = 1024
        self.is_running = False

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        self.is_running = True
        print("Server start")

    def accept_client(self):
        self.conn, self.addr = self.server.accept()
        print("Client connected by ", self.addr)

    def receive(self):
        data = self.conn.recv(self.max_message_size)
        return data.decode()

    def send(self, text):
        self.conn.send(str(text).encode())

    def close_client(self):
        if self.conn:
            self.conn.close()
            print(f"Client {self.addr} disconnected")
        self.conn = None
        self.addr = None

    def stop(self):
        self.close_client()
        if self.server:
            self.server.close()
        self.server = None
        self.is_running = False
        print("Server closed")