import socket

# Server settings
host = '127.0.0.1'  # Localhost
port = 12345         # Port to bind to

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind((host, port))

# Start listening for connections (max 1 client in the queue)
server_socket.listen(1)

print(f"Server is listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Send a welcome message to the client
client_socket.send(b"Hello, client!")

# Receive data from the client
client_data = client_socket.recv(1024)
print(f"Received from client: {client_data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()
