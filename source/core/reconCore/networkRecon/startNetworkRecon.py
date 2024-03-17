import os
from .netToolAttacks import nmap
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


def hold():
    input('debug hold')


class WifiScan:

    def __init__(self, master: list):
        self.ips = master
        """here to check if connected. I supply the ip of the device this is running on"""

        # if we have an ip address, we set master to True
        if len(master[0]) < 1:
            master = False
        else:
            master = True

        # now we check if connected
        if not self.isConnected(master):
            input('[!] not connected to network press enter to exit')
            return
        self.startWirelesMenu()

    @staticmethod
    def isConnected(pram):
        if pram:
            return True
        return False

    def startWirelesMenu(self):
        while True:
            try:
                os.system("clear")
                data = input(f"""1.) show connected devices
2.) show individual device info
3.) use traceroute to scan for more networks
4.) use custom python script
0.) back
[Welcome to AMS Network recon mode]: """)

                def Reader(ips):
                    ip = self.ips[0][0]
                    sub = self.ips[1][0]
                    os.system(f"nmap -A {ip}/{sub}")
                    return

                def TraceRoute(ip):
                    ipp = ip[0][0].split(".")[0:3]
                    s = ''
                    for x in ipp:
                        s += f"{x}."
                    s += "1"
                    print(s)
                    if "traceroute" not in os.listdir("/bin"):
                        os.system("sudo apt-get install inetutils-traceroute")
                    os.system(f"traceroute {s}")
                    input()
                    return

                def script(ip):
                    ip = None
                    os.chdir("scripts")
                    for x in os.listdir(os.getcwd()):
                        print(x)
                    os.system(f"python3 {input('Please enter the script')}")

                funcs = ["return", nmap, Reader, TraceRoute, script]
                try:
                    if int(data) == 0:
                        return

                    f = funcs[int(data)](self.ips)
                except ValueError:
                    continue

            except KeyboardInterrupt:
                return




