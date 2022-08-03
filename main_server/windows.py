import paho.mqtt.client as mqtt
import json
import pandas as pd
import nmap
import netifaces as ni
import winreg as wr
from pprint import pprint

message = 0
main_topic = "topic/hospital"
status_topic = "topic/status"
broker_ip = "192.168.43.52"

df = pd.read_excel('conversion_table.xlsx')
prefix_length = df['CIDR prefix length'].tolist()
decimal_netmask = df['Dotted Decimal Netmask'].tolist()
conversion_dictionary= dict(zip(decimal_netmask, prefix_length))

def get_connection_name_from_guid(iface_guids):
    iface_names = ['(unknown)' for i in range(len(iface_guids))]
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'\Connection')
            iface_names[i] = wr.QueryValueEx(reg_subkey, 'Name')[0]
        except FileNotFoundError:
            pass
    return iface_names

def get_ip_with_cidr():
    global adapters_name
    network_address = ''
    x = ni.interfaces()
    name_list = get_connection_name_from_guid(x)
    index = name_list.index("Wi-Fi")
    info = ni.ifaddresses(x[index])
    netmask_value = info[ni.AF_INET][0]['netmask']
    ip_address = info[ni.AF_INET][0]['addr']
    _ = ip_address.split(".")
    for i in range(3):
        network_address = network_address + _[i] + "."
    network_address = network_address + '1'
    res = network_address + conversion_dictionary[netmask_value]
    return res

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
    def __init__(self, ip=""): 
        ip = get_ip_with_cidr()
        self.ip = ip
        print(self.ip)

    def network_scanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip
        print("scanning network")
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print("Host\t{}".format(host))

D = Network()
D.network_scanner()

# get_ip_with_cidr()


# while True:
#     # awaiting_message()
#     time.sleep(2)
#     publish_message()

# battery, status (busy or not)
