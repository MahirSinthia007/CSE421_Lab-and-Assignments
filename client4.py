import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
PORT=65333

client.connect((HOST,PORT))

hours = input("Enter hours worked: ")
client.send(hours.encode('UTF-8'))

salary = client.recv(1024).decode('UTF-8')
print("Calculated Salary:", salary)

client.close()
