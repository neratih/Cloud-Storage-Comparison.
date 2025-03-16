import socket

# Client settings
host = '127.0.0.1'  # Server address
port = 12345         # The same port as the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Receive data from the server
server_message = client_socket.recv(1024)
print(f"Received from server: {server_message.decode()}")

# Send a response to the server
client_socket.send(b"Hello, server!")

# Close the connection
client_socket.close()
