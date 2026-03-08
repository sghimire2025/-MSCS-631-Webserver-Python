# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(('', 6789))  # Bind to port 6789
serverSocket.listen(1)  # Listen for incoming connections (max 1 queued connection)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    
    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start #Fill in end
        
        # Check if message is not empty and has proper format
        if not message or len(message.split()) < 2:
            connectionSocket.close()
            continue
            
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Fill in start #Fill in end
        
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        # Fill in end
        
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        
        f.close()
        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Fill in end
        
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data