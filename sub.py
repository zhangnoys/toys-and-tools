import threading
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import json
import time
from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='DC:A6:32:B0:6A:54',
        device_addr='C7:E7:B2:0F:91:04',
                         accelerometer_service=True,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=True)
looping = True
str1='1'
str2='1'
str3='1'
ubit.connect()
stop_threads = False
#get subscibe form server
def delay():
    while 1:
        msg = subscribe.simple("delay", hostname="10.83.196.154")
        global str1
        str1 = msg.payload.decode('UTF-8')
        print(int(str1))
def delay2():
     while 1:
        msg2 = subscribe.simple("delayX", hostname="10.83.196.154")
        global str2
        str2 = msg2.payload.decode('UTF-8')
        print(int(str2))    
def delay3():
     while 1:
        msg3 = subscribe.simple("delayT", hostname="10.83.196.154")
        global str3
        str3 = msg3.payload.decode('UTF-8')
        print(int(str3))  





# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("commond")
def test():

    while looping:
            x, y, z = ubit.accelerometer
            print('Temperature:', ubit.temperature)
            data = { "id" : "microbit", "temp" : ubit.temperature, "hum" : 12,"xx":x,"yy":y,"zz":z } 
            data2 = json.dumps(data)
            publish.single("sensor", data2, hostname="10.83.196.154")
            print(data2)
            time.sleep(int(str1))
def test1():

    while looping1:
            x, y, z = ubit.accelerometer
            data = { "id" : "microbit","xx":x,"yy":y,"zz":z } 
            data2 = json.dumps(data)
            publish.single("sensor", data2, hostname="10.83.196.154")
            print(data2)
            time.sleep(int(str2))

def test2():

    while looping2:
            print('Temperature:', ubit.temperature)
            data = { "id" : "microbit", "temp" : ubit.temperature, "hum" : 12 } 
            data2 = json.dumps(data)
            publish.single("sensor", data2, hostname="10.83.196.154")
            print(data2)
            time.sleep(int(str3))
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload==b'on':
        global looping
        looping = True
        thread = threading.Thread(target=test)
        thread.start()
    if msg.payload==b'off':
        looping = False
        print("off")
    if msg.payload==b'X_on':
        global looping1
        looping1 = True
        thread = threading.Thread(target=test1)
        thread.start()
    if msg.payload==b'X_off':
        looping1 = False
        print("off")    
    if msg.payload==b'T_on':
        global looping2
        looping2 = True
        thread = threading.Thread(target=test2)
        thread.start()
    if msg.payload==b'T_off':
        looping2 = False
        print("off")       
#multithreading start        
client = mqtt.Client()
thread = threading.Thread(target=delay)
thread.start()
thread = threading.Thread(target=delay2)
thread.start()
thread = threading.Thread(target=delay3)
thread.start()
#start thread which to start sub from mqtt server
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.83.196.154", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
