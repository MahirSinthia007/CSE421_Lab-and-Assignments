import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST= socket.gethostbyname(socket.gethostname())
PORT=65333

client.connect((HOST,PORT))

data = f"IP: {HOST}, Device Name {socket.gethostname()}"
client.send(data.encode('UTF-8'))

client.close()

