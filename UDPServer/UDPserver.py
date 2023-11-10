import socket

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# bind the socket to a specific address and port
server_address = ('localhost', 12000)
sock.bind(server_address)

while True:
    print('waiting for message...')
    data, address = sock.recvfrom(4096)

    print(f'received {len(data)} bytes from {address}')
    print(f'data: {data.decode()}')

    # send a response back to the client
    message = 'pong'
    sock.sendto(message.encode(), address)

    print(f'sent {len(message)} bytes back to {address}')