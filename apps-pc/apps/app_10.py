import paho.mqtt.client as mqtt
import subprocess
import random
from random import randint
import os
import time
#app should be able to modify aclfile dynamically.

# The callback for when the client receives a CONNACK response from the server.
control = ["on", "off"]
totalTime = 0.0
count = 0
def on_connect(client, userdata, flags, rc):
    print("on_connect,hehe")
    #print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("sensors/device_10/control")
    client.subscribe("sensors/device_10")
    #client.subscribe("#")
#    client.subscribe("a/b")

def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index
def propobility():
    rate = [20, 80]
    #20% retained, 80% not.
    #for x in range(1, 5):#print 4 times of 1 or 0.
    print(random_index(rate)) #print 1 or 0.
        
def modify_aclfile(filepath):
    #append:
    file = open(filepath, "a")
    file.write("\nuser app_10")
    i = randint(1, 500)
    file.write("\nsensors/device_" + str(i))
    strr = "sensors/device_" + str(i)
    # file.write("\nsensors/device_" + str(i) + "/control")
    # strr = "sensors/device_" + str(i) + "/control"
    file.close()
    return strr
#modify dynamically and randomly.
def pub_command():
    control = ["on", "off"]
    #
    # time.sleep(2)
    # published = control[randint(0,1)]
    # client.publish(topic="sensors/device_10/control", payload = published, retain=True)
    #print(published)
    rate = [99, 1]
    if(random_index(rate) == 1):
        print("modify aclfile")

        #modify_aclfile("/Users/zhaodo/Library/Mobile Documents/com~apple~CloudDocs/Documents/Lab/IoT/YanJiaProject/mosquitto/MQTT_defense/conf/aclfile")
        ####### return value!!!
        topic_new = modify_aclfile("yue's Mac/aclfile")
        client.subscribe(topic_new)
        #-----!!!
        # if(append topic auth) if (delete topic auth)
        # client.unsubscribe(topic_new)
        # client.subscribe(topic_new)
        #-----
        subprocess.run(["kill", "-HUP", "95407"])

def output_aver(outputFile, inputMsg):#"separate_aver.txt"
    print("executed")
    aver_file = open(outputFile, "a")
    aver_file.write(inputMsg)
    aver_file.close()
#The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("Received")
    #print("Received: " + msg.topic+" "+str(msg.payload))
    global count
    global totalTime
    print("on_message:")
    currentTime = time.time()
    #print(float(str(msg.payload)))
    print(msg.payload)
    print(currentTime)
    #timeLag = currentTime * 1000000 - float(str(msg.payload)[2:20])
    timeLag = currentTime - float(msg.payload)
    print("timeLag: ", timeLag)
    #timeLag = currentTime - float(str(msg.payload)[2:20])
    #print("Received, time lag: " + msg.topic+" " + str(timeLag))###
    ##print("Received, time lag: %s, count is %d" % (str(timeLag), count))
    # print(totalTime)
    count += 1
    if count > 10:
        totalTime = totalTime + timeLag
        # print("totalTime is: ", str(totalTime))  
        print(count - 10)
        aver = totalTime/(count-10)
        #print(totalTime/(count-10))
        print(aver)
        if (count-10) == 30: # after 5 * 60 s ??
            print("average file.")
            aver_file = open("./separate_aver.txt", "a")
            aver_file.write("\n" + str(aver))
            aver_file.close()


    #pub_command()

client = mqtt.Client(client_id="control_app_10", clean_session = False)
#client.username_pw_set(username = "app_10", password = None)
client.username_pw_set(username = "app_10", password = None)
client.on_connect = on_connect
client.on_message = on_message
#client.will_set(topic="sensors/sensor-3542/control", payload="Client_4:last will message!" + str(time.time()), qos=0, retain=False)

#client.connect("127.0.0.1", 1883, 60)
client.connect("156.56.159.126", 1883, 60)
#client.subscribe("a/a")
#client.publish(topic="sensors/device_10/control", payload = "app msg", retain=True)

#pub_command()

#client.publish(topic="sensors/sensor-3542/control", payload = "open", retain=True)

#client.publish(topic="a/b", payload = "B:bbbbbbbbbb"+str(time.time()), retain=True)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
