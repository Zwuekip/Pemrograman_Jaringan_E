import sys
import socket

sock_alpine_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_alpine_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alamat_server_alpine_1 = ('192.168.122.64', 10000)
print(f"connecting to {alamat_server_alpine_1}")
sock_alpine_1.connect(alamat_server_alpine_1)
alamat_server_alpine_2 = ('192.168.122.141', 10000)
print(f"connecting to {alamat_server_alpine_2}")
sock_alpine_2.connect(alamat_server_alpine_2)

try:
    # Send data image
    msg = open("maxresdefault.jpg", 'rb')
    msg_read = msg.read()
    print(f"sending {msg}")
    sock_alpine_1.sendall(msg_read)
    sock_alpine_2.sendall(msg_read)
    jumlah_diterima_alpine_1 = 0
    jumlah_tak_terduga_alpine_1 = len(msg_read)
    file_alpine_1 = bytearray()
    while jumlah_diterima_alpine_1 < jumlah_tak_terduga_alpine_1:
        data_alpine_1 = sock_alpine_1.recv(16)
        jumlah_diterima_alpine_1 += len(data_alpine_1)
        file_alpine_1 += data_alpine_1
        print("dari alpine 1: ", f"{data_alpine_1}")
    
    write_alpine_1 = open("Neil_Coffe_Talk1.jpg", 'wb')
    write_alpine_1.write(file_alpine_1)
    write_alpine_1.close()
    jumlah_diterima_alpine_2 = 0
    jumlah_tak_terduga_alpine_2 = len(msg_read)
    file_alpine_2 = bytearray()
    while jumlah_diterima_alpine_2 < jumlah_tak_terduga_alpine_2:
        data_alpine_2 = sock_alpine_2.recv(16)
        jumlah_diterima_alpine_2 += len(data_alpine_2)
        file_alpine_2 += data_alpine_2
        print("dari alpine 2: ", f"{data_alpine_2}")

    write_alpine_2 = open("Neil_Coffe_Talk2.jpg", 'wb')
    write_alpine_2.write(file_alpine_2)
    write_alpine_2.close()

finally:
    print("closing")
    sock_alpine_1.close()
    sock_alpine_2.close()