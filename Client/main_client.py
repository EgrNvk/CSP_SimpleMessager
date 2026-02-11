from Client.Model.model_client import Client

HOST = '127.0.0.1'
PORT = 4000


client = Client(HOST, PORT)
client.connect()
print("Connected to server. Type 'exit' to quit.")

while True:
    text=input("Client: ")

    if text.lower() == "exit":
        client.send(text)
        client.disconnect()
        print("Disconnected.")
        break

    client.send(text)

    reply = client.receive()
    if reply:
        print("Server: ", reply)