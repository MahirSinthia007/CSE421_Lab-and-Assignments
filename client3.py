import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST= socket.gethostbyname(socket.gethostname())
PORT=65333

client.connect((HOST,PORT))
msg=input("Enter your message: ")
client.send(msg.encode('UTF-8'))
reply=client.recv(1024).decode('UTF-8')
print("Server says ", reply)

client.close()
