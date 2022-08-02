from sys import prefix
import paho.mqtt.client as mqtt
import scapy.all as scapy
import argparse
import os
import time
import socket
import json
import subprocess
import pandas as pd
import ifaddr
import nmap
from ipaddress import ip_address, IPv4Address

message = 0
main_topic = "topic/hospital"
status_topic = "topic/status"
broker_ip = "192.168.43.52"

df = pd.read_excel('conversion_table.xlsx')
prefix_length = df['CIDR prefix length'].tolist()
decimal_netmask = df['Dotted Decimal Netmask'].tolist()
conversion_dictionary= dict(zip(prefix_length, decimal_netmask))

def get_ip_with_cidr():
    adapters = ifaddr.get_adapters()
    device_adapters = []
    main_list = []
    ipv4_address_list = []
    for adapter in adapters:
        device_adapters.append(adapter.nice_name)
        for ip in adapter.ips:
            main_list.append("   %s/%s" % (ip.ip, ip.network_prefix))
    ip_with_cidr = main_list[1:][::2]
    for i in ip_with_cidr:
        if type(ip_address(i)) is IPv4Address:
            ipv4_address_list.append(i)
    for i in device_adapters:
        if "Wireless" in i:
            index = device_adapters.index(i)
            break
    return ip_with_cidr[index]

def conversion_to_subnet_mask(ip_address):
    split_string = ip_address.split("/")
    res = conversion_dictionary["/" + split_string[1]]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Standby")
    client.subscribe(topic)
def on_message(self, client, userdata, msg):
    global message
    message = msg.payload.decode()
    print(message)
    client.disconnect()

class mqtt_operation():
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        print("Standby")
        client.subscribe(main_topic)
    def on_message(self, client, userdata, msg):
        self.message = msg.payload.decode()
        print(self.message)
        client.disconnect()
    def extract_dictionary(self, dict):
        self.data = json.loads(dict)
        self.doctor = self.data["doctor_name"]
        self.patient = self.data["patient_number"]
        self.medicine = list(self.data["medicine"])
        self.amount  = list(self.data["amount"])
        self.medicine_prescription = []
        for i in range(3):
            self.medicine_prescription.append((self.medicine[i], self.mount[i]))
        print("Doctor: ", self.doctor)
        print("Patient: ", self.patient)
        print("medicine:")
        for i in range(3):
            print(self.medicine[i] + ": " + self.amount[i])
    def awaiting_message():
        client = mqtt.Client()
        client.connect(broker_ip,1883)
        client.on_connect = on_connect
        client.on_message = on_message
        client.loop_forever()
        client.disconnect()
    def publish_message():
        client = mqtt.Client()
        client.connect(broker_ip,1883)
        client.publish(status_topic, "Done")
        client.disconnect()

class Robot():
    pass

class Network(object):
    def __init__(self): 
        self.ip = get_ip_with_cidr()
        print(self.ip)
    def network_scanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        print("scanning network")
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print("Host\t{}".format(host))

D = Network()
D.network_scanner()



# while True:
#     # awaiting_message()
#     time.sleep(2)
#     publish_message()

# battery, status (busy or not)
