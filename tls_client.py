# client side
# echo client
from socket import *
from ssl import *

# user is not finnished
finnished = False

# create socket
client_socket = socket(AF_INET, SOCK_STREAM)
tls_client = wrap_socket(client_socket, ssl_version=PROTOCOL_TLSv1, cert_reqs=CERT_REQUIRED,
                         keyfile='client/client.pem', certfile='client/client.crt', ca_certs='server/server.crt')

# connect to the echo server
tls_client.connect(('127.0.0.1', 6668))

if __name__ == '__main__':
    # while not finished
    while not finnished:
        # message
        message = 'hello world!'
        data_out = message.encode()

        # send data out
        tls_client.send(data_out)

        # receive data
        data_in = tls_client.recv(1024)

        # decode message
        response = data_in.decode()
        print('Received from client:', response)

        reapet = input('yes or no?  ')

        if reapet == 'n':
            finnished = True
            tls_client.send(b'quit')

    # close the socket
    tls_client.shutdown(SHUT_RDWR)
    tls_client.close()
