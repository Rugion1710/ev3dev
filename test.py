import nmap
import socket

class Network(object):
    def __init__(self, ip=""):
        ip = input("enter value")
        self.ip = ip
    
    def network_scanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip + '/24'
        print(type(network))
        print("scanning network")
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print("Host\t{}".format(host))

D = Network()
D.network_scanner()