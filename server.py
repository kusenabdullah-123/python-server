import socket
import json

# Define socket host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080
database = [
    {
        'nama': 'mei',
    }, {
        'nama': 'mei pro',
    }
]
# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()
print(f'Listening on port {SERVER_PORT}')

while True:

    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(2048).decode()
    req = request.split('\r\n')[0].split(' ')
    if req[0] == 'GET':
        if req[1] == '/users':
            client_connection.send(f'{req[2]} 200 OK\r\n'.encode())
            client_connection.send(
                'Content-Type : application/json\r\n\r\n'.encode())
            client_connection.send(json.dumps(database).encode())
    client_connection.close()

# Close socket
server_socket.close()
