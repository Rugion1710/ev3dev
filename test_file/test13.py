import socket

a = socket.gethostbyaddr("192.168.43.38")
print(a[0])