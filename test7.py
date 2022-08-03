import ifaddr
import ipaddress
list = []
adapters = ifaddr_test.get_adapters()

for adapter in adapters:
    print("IPs of network adapter " + adapter.nice_name)
    for ip in adapter.ips:
        print("   %s/%s" % (ip.ip, ip.network_prefix))
        try:
            if type(ipaddress.ip_network(ip)) is tuple:
                pass
            else:
                list.append(ip)
        except:
            print("invalid")

print(list)