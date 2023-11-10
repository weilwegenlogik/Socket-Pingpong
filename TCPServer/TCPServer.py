import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 12000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode() == "ping":
                conn.sendall(b"pong")
