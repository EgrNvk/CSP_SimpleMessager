class ServerController:
    def __init__(self, view, server):
        self.view = view
        self.server = server

        self.view.btn_send.configure(command=self.on_send_click)
        # self.view.entry.bind("<Return>", self.on_send_click)

        self.running = False
        self.has_client = False

    def start(self):
        try:
            if self.server.server_socket is None:
                self.server.start()
                self.server.server_socket.setblocking(False)
                self.view.add_line("SYSTEM: Server started")
        except:
            self.view.add_line("SYSTEM: Server not started")
            self.view.btn_send.config(state="disabled")
            self.view.root.after(5000, self.start)
            return

        self.view.btn_send.config(state="disabled")
        self.poll_accept()

    def poll_accept(self):
        if self.has_client:
            return

        try:
            self.server.accept_client()
            self.server.client_socket.setblocking(False)
            self.has_client = True
            self.running = True

            self.view.add_line("SYSTEM: Client connected")
            self.view.btn_send.config(state="normal")

            self.poll_receive()

        except:
            self.view.root.after(200, self.poll_accept)

    def on_send_click(self, event=None):
        text = self.view.entry.get()
        if text == "":
            return

        self.view.add_line("Server: " + text)
        self.view.entry.delete(0, "end")

        self.server.send(text)

    def poll_receive(self):
        try:
            msg=self.server.receive()

            if msg =="_offline_":
                self.client_disconnect("SYSTEM: Client disconnected")
                return
            if msg:
                self.view.add_line("Client: " + msg)

        except:
            pass

        self.view.root.after(50, self.poll_receive)

    def client_disconnect(self, system_text):
        self.view.add_line(system_text)

        self.running = False
        self.has_client = False
        self.view.btn_send.config(state="disabled")

        try:
            self.server.disconnect_client()
        except:
            pass


        self.view.root.after(200, self.poll_accept)