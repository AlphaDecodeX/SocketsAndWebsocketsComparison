import asyncio
from websockets import serve

async def send_message(websocket):
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
    await websocket.send(res)

async def main():
    print("Server is listening.....")
    async with serve(send_message, "localhost", 8080):
        await asyncio.Future()

asyncio.run(main())