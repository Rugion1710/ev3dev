import ifaddr

adapters = ifaddr.get_adapters()
device_adapters = []
main_list = []
for adapter in adapters:
    device_adapters.append(adapter.nice_name)
    for ip in adapter.ips:
        main_list.append("   %s/%s" % (ip.ip, ip.network_prefix))

print(device_adapters)
ip_with_cidr = main_list[1:][::2]
print(ip_with_cidr)
# print(list[0:][::2])
# print(list[1:][::2])
