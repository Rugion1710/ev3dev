from scapy.all import *

def arp_scan(ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, unans = srp(request, timeout=2, retry=1)
    result = []
    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})
    return result

print(arp_scan("192.168.43.1/24"))
# for i in range(len(result)):
#     for x in range(2)