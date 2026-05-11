import socket
import threading

def count_vowels(text):
    vowels = "aeiouAEIOU"
    sum=0
    for ch in text:
        if ch in vowels:
            sum=sum+1
    return sum
def handel_client(conn,addr):
   

   msg=conn.recv(1024).decode('UTF-8')
   v = count_vowels(msg)

   if v==0:
        reply= "Not enough vowels"

   elif 1<=v<=2:
        reply= "Enough vowels i guess"
    
   elif v>2:
        reply = "Too many vowels"

   conn.send(reply.encode('UTF-8'))
   conn.close()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
PORT=65333
server.bind((HOST,PORT))
server.listen(2)

while True:
    conn,addr=server.accept()
    thread=threading.Thread(target=handel_client,args=(conn,addr))
    thread.start()
