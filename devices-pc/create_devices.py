#/Users/zhaodo/Library/Mobile Documents/com~apple~CloudDocs/Documents/Lab/IoT/YanJiaProject/mosquitto/MQTT_defense/scripts
import os

def create_app_scripts(filepath, n):
    for i in range(1, n+1):
        file = open("app_1.py", "r")
        f = open(filepath + "app_" + str(i) + ".py", "a")
        while 1:
            lines = file.readlines(500)
            if not lines:
                break
            for line in lines:
                if "app_1" in line:
                    f.write(line.replace("app_1", "app_" + str(i)))
                    print("written")
                else:
                    if "device_1" in line:
                        f.write(line.replace("device_1", "device_" + str(i)))
                    else:
                        f.write(line)
        f.close()
        file.close()
def create_device_scripts(filepath, n):
    for i in range(1, n+1):
        file = open("device_1.py", "r")
        f = open(filepath + "device_" + str(i) + ".py", "a")
        while 1:
            lines = file.readlines(500)
            if not lines:
                break
            for line in lines:
                if "app_1" in line:
                    f.write(line.replace("app_1", "app_" + str(i)))
                else:
                    if "device_1" in line:
                        f.write(line.replace("device_1", "device_" + str(i)))
                    else:
                        f.write(line)
        f.close()
        file.close()
def set_aclfile(filename, n):
    file = open(filename, "a")
    for i in range(1, n + 1):
        file.write("\nuser app_" + str(i))
        file.write("\ntopic sensors/device_" + str(i))
        pass
    file.close()
#create_app_scripts("./apps/", 1000)
create_device_scripts("./devices/", 1000)
#set_aclfile("/Users/Ceshi/Downloads/mosquitto/conf/aclfile", 500)
