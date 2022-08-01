#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import ev3dev2.fonts as fonts
import paho.mqtt.client as mqtt
import os
import time
import json

message = 0
topic = "topic/hospital"
topic2 = "topic/status"

def decoding(message):
    object = message.decode()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("Standby")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    global message
    message = msg.payload.decode()
    print(message)
    client.disconnect()

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
    print("Patient: ", patient)s
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
    client.connect("test.mosquitto.org",1883)
    client.publish(topic2, "Done")
    client.disconnect()

def program():
    pass

while True:
    awaiting_message()
    program()
    time.sleep(2)
    publish_message()