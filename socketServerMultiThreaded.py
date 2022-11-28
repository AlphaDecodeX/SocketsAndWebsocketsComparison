import socket, threading
class ClientRequestThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.clientSocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        myfile = 'index.html'    # Take index.html as filename
        try:
            file = open(myfile,'rb') # Read in byte format
            response = file.read()
            file.close()
            head = 'HTTP/1.1 200 OK\n'
            head += 'Content-Type: '+'text/html'+'\n\n'
        except Exception as e:
            head = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><h1>404 Not Found</h1></body></html>'.encode('utf-8')
        res = head.encode('utf-8')
        res += response
        self.clientSocket.send(res)
        self.clientSocket.close()

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request.....")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientRequestThread(clientAddress, clientsock)
    newthread.start()