import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
PORT=65333

client.connect((HOST,PORT))
data = input("Enter a message: ")
client.send(data.encode('UTF-8'))

reply=client.recv(1024)
reply=reply.decode('UTF-8')
print("Server says: ", reply)

client.close()

