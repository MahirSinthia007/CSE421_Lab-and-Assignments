import socket

HOST=socket.gethostbyname(socket.gethostname())
PORT=65333
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(2)

while True:
    conn,addr=server.accept()
    print("client connected",addr)

    hours=int(conn.recv(1024).decode('UTF-8'))
    if hours <=40:
        salary=hours*200
    else:
        salary=8000+(hours-40)*30

    conn.send(str(salary).encode('UTF-8'))
    conn.close()