import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alamat_server = ('192.168.122.64', 10000) # untuk alpine 1
#alamat_server = ('192.168.122.141', 10000) # untuk alpine 2
print(f"starting up on {alamat_server}")
sock.bind(alamat_server)
sock.listen(1)
while True:
    print("waiting for a connection")
    connection, alamat_client = sock.accept()
    print(f"connection from {alamat_client}")
    while True:
        data = connection.recv(1024)
        print(f"received {data}")
        if data:
            print("sending back data")
            connection.sendall(data)
        else:
            break
    connection.close()