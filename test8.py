import ipaddress
print(type(ipaddress.ip_network('192.168.100.0/24')))

if type(ipaddress.ip_network('192.168.100.0/24')) is ipaddress.IPv4Network:
    print("true")

