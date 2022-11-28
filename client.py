import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

file = open("test1.txt", 'wb')        
recvData = client.recv(1024)
while recvData:
    file.write(recvData)
    recvData = client.recv(1024)
client.close()