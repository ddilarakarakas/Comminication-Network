# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

SERVER_PORT = 8080
BUFFER_SIZE = 1024
# Prepare a server socket
# Fill in start
serverSocket.bind(("", SERVER_PORT))
serverSocket.listen(1)

print(gethostname(), "  ", gethostbyname(gethostname()))
print("Web server is started. Port number : ", SERVER_PORT)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(BUFFER_SIZE)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(bytes('\HTTP/1.0 200 OK\r\n\r\n'.encode()))
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i].encode()))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(bytes('\HTTP/1.0 200 404 NOT FOUND\r\n\r\n'.encode()))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()))
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()

# 127.0.0.1:8080/HelloWorld.html   or localhost:8080/HelloWorld.html
