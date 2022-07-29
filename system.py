import paho.mqtt.client as mqtt
import scapy.all as scapy
import argparse
import os
import time
import socket
import json
import subprocess

message = 0
topic = "topic/hospital"
topic2 = "topic/status"
checklist = range(256)

for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")



def get_IPAddress():
    

class mqtt_operation(self):

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        print("Standby")
        client.subscribe(topic)
    def on_message(self, client, userdata, msg):
        global message
        message = msg.payload.decode()
        print(message)
        client.disconnect()

class robot(self):
    self.ip_address = 



def extract_dictionary(dict):
    data = json.loads(dict)
    doctor = data["doctor_name"]
    patient = data["patient_number"]
    medicine = list(data["medicine"])
    amount  = list(data["amount"])
    medicine_prescription = []
    for i in range(3):
        medicine_prescription.append((medicine[i], amount[i]))
    print("Doctor: ", doctor)
    print("Patient: ", patient)
    print("medicine:")
    for i in range(3):
        print(medicine[i] + ": " + amount[i])

def awaiting_message():
    client = mqtt.Client()
    client.connect("test.mosquitto.org",1883)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
    client.disconnect()

def publish_message():
    client = mqtt.Client()
    client.connect("192.168.43.52",1883)
    client.publish(topic2, "Done")
    client.disconnect()

while True:
    # awaiting_message()
    time.sleep(2)
    publish_message()

# battery, status (busy or not)
