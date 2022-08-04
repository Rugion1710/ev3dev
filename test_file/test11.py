from scapy.all import *
list1 = []
list2 = []

ans,unans = arping("192.168.43.1/24", verbose=0)
for s,r in ans:
    list1.append(r[Ether].src)
    list2.append(s[ARP].pdst)
    print("{} {}".format(r[Ether].src,s[ARP].pdst))

print(list1)
print(list2)





# ans,unans = arping("10.183.1.1/24", verbose=0)
# for s,r in ans:
#     print("{} {}".format(r[Ether].src,s[ARP].pdst))
