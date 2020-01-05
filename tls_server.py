# server side
# echo client
from socket import *
from ssl import *

# create socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind to an unused port on the local machine
server_socket.bind(('127.0.0.1', 6668))

# listen for connection
server_socket.listen(1)
tls_server = wrap_socket(server_socket, ssl_version=PROTOCOL_TLSv1, server_side=True, cert_reqs=CERT_REQUIRED,
                         keyfile='server/server.pem', certfile='server/server.crt', ca_certs='client/client.crt')


print('server started')

# accept connection
connection, client_address = tls_server.accept()
print('connection from', client_address)

# server is not finnished
finished = False

if __name__ == '__main__':
    # while not finnished
    while not finished:
        # send and receive data from the client socket
        data_in = connection.recv(1024)
        message = data_in.decode()
        print('client send', message)

        if message == 'quit':
            finnished = True
        else:
            data_out = message.encode()
            connection.send(data_out)
