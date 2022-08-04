# import ifaddr
# import ipaddress

# adapters = ifaddr.get_adapters()

# for adapter in adapters:
#     print("IPs of network adapter " + adapter.nice_name)
#     for ip in adapter.ips:
#         print("   %s/%s" % (ip.ip, ip.network_prefix))
#         print(type(ip))
#         # if type(ipaddress.ip_network(ip)) is ipaddress.IPv4Network:
#         #     print("true")
#         # else:
#         #     print('false')

import socket
print(socket.gethostbyname(socket.gethostname()))