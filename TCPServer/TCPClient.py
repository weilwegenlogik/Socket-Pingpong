import socket

# Define the server address and port
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 12000

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send the ping request
ping_request = b'ping'
client_socket.sendall(ping_request)

# Receive the response
response = client_socket.recv(1024)

# Print the response
print(response.decode())

# Close the socket
client_socket.close()
