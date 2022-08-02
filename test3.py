import socket
import ipaddr
mask = ipaddr.IPv4Network('192.192.45.1/25')
mask.netmask

iface = "eth0"
socket.inet_ntoa(
fcntl.ioctl(socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM), 35099, 
struct.pack('256s', iface))[20:24])