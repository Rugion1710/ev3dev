import ifaddr
import ipaddress
list = []
adapters = ifaddr.get_adapters()

for adapter in adapters:
    print("IPs of network adapter " + adapter.nice_name)
    for ip in adapter.ips:
        print("   %s/%s" % (ip.ip, ip.network_prefix))
        try:
            if type(ipaddress.ip_network(ip)) is ipaddress.IPv4Network:
                list.append(ip)
        except:
            print("invalid")

print(list)