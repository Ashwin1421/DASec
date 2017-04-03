import socket

server_socket = socket.socket()
server_host = socket.gethostname()
server_port = 8899
server_socket.bind((server_host,server_port))
server_socket.listen(10)
while True:
    server_accept,addr = server_socket.accept()
    print('Connected to',addr)
    server_accept.send(b'Hello')
    server_accept.close()
