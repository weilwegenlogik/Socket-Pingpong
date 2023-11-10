import socket

# Set up the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the server address and port
server_address = ('localhost', 12000)

# Send the ping request
message = b'ping'
client_socket.sendto(message, server_address)

# Receive the response
data, server = client_socket.recvfrom(1024)
print(f'Received "{data.decode()}" from {server}')

# Close the socket
client_socket.close()
