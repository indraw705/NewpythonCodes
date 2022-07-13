import paramiko
import time
import string
import random

hostname = "10.115.124.231"
# hostname = "10.115.140.44"
# hostname = "10.115.98.249"
username = "root"
# password = "edrqa@123"
password = "Password123"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()


def ProduceFileEvents():
    for i in range(30):
        print("=" * 50, "------fileEvent " + str(i) + "-----", "=" * 50)
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        print(res)
        client.exec_command("mkdir /opt/" + res)
        client.exec_command("cp /opt/INDRAJIT/crickbuzz.py /opt/" + res)
        time.sleep(10)
        # client.exec_command("mv /opt/" + res + "/JIOBROADBAND.py /opt/" + res + "/" + res + ".py")
        client.exec_command("python3.6 /opt/INDRAJIT/crickbuzz.py ")


def ProduceNetworkEvents():
    for i in range(10):
        print("=" * 50, "------ProcessNetworkEvent " + str(i) + "-----", "=" * 50)
        client.exec_command("netstat -r")
        time.sleep(2)
        client.exec_command("arp -e")
        time.sleep(2)
        client.exec_command("ping 10.44.76.188 -c 1000")
        time.sleep(2)
        client.exec_command("nmcli device status")
        client.exec_command("ss -l")
        client.exec_command("tracepath google.com")
        time.sleep(8)
        client.exec_command("tracepath amazon.com")
        time.sleep(8)
        client.exec_command("tracepath realme.com")
        time.sleep(8)
        client.exec_command("id")
        time.sleep(8)
        client.exec_command("whoami")
        time.sleep(8)


# ProduceFileEvents()
ProduceNetworkEvents()

