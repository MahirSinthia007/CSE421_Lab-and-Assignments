import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
PORT=65333
server.bind((HOST, PORT))

server.listen(2)
print("Server running on port 65333")

while True:
    conn, addr = server.accept()
    print("Connected with:", addr)

    data = conn.recv(1024).decode()
    print("Client Info:", data)

    conn.close()
