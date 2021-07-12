import sys
import socket
import random
import string

sock_alpine1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_alpine2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alamat_server_alpine1 = ('192.168.122.64', 10000) # IP alpine 1
print(f"connecting to {alamat_server_alpine1}")
sock_alpine1.connect(alamat_server_alpine1)
alamat_server_alpine2 = ('192.168.122.141', 10000) # IP alpine 2
print(f"connecting to {alamat_server_alpine2}")
sock_alpine2.connect(alamat_server_alpine2)

try:
    msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"sending {msg}")
    sock_alpine1.sendall(msg.encode())
    jumlah_diterima = 0
    jumlah_tak_terduga = len(msg)
    while jumlah_diterima < jumlah_tak_terduga:
        data = sock_alpine1.recv(16)
        jumlah_diterima += len(data)
        print(f"{data}")

    msg2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"sending {msg2}")
    sock_alpine2.sendall(msg2.encode())
    jumlah_diterima2 = 0
    jumlah_tak_terduga2 = len(msg2)
    while jumlah_diterima2 < jumlah_tak_terduga2:
        data2 = sock_alpine2.recv(512)
        jumlah_diterima2 += len(data2)
        print(f"{data2}")

finally:
    print("closing")
    sock_alpine1.close()
    sock_alpine2.close()