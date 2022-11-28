import asyncio, socket

async def handle_client(client):
    loop = asyncio.get_event_loop()
    print("Client Accepted ", client)
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
    await loop.sock_sendall(client, res)
    client.close()

async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    print("Server is listening.....")
    server.listen(4000)
    server.setblocking(False)

    loop = asyncio.get_event_loop() # Event loops runs async tasks, perform network IO

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client)) # Create async tasks and run

asyncio.run(run_server())