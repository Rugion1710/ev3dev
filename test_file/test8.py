import ipaddress 

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address)) 
if type(ipaddress.ip_network('127.0.0.1/8')) is ipaddress.IPv4Network:
    print("true")

