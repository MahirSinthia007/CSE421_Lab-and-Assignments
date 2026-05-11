import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
PORT=65333
server.bind((HOST,PORT))
server.listen(2)

while True:
    conn,addr = server.accept()
    print("Connected with", addr)
    
    data= conn.recv(1024).decode('UTF-8')
    print("Client info: ", data)
    
    conn.close()