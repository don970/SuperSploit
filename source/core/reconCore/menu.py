import os
import subprocess
from .networkRecon import WifiScan
from .Bluetooth import bt

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


class menu:
    INPUT = None

    def __init__(self):
        while True:
            self.INPUT = self.startMenu()
            if self.startChoice():
                continue
            else:
                return

    def getMyInfo(self):
        ipList = []
        ip = subprocess.run(['ip', 'addr'], capture_output=True)
        ip = ip.stdout.decode().split('\n')
        for x in ip:
            if 'inet' in x and 'brd' in x:
                ipList.append(x)
        ip = ipList
        ipList = []
        subnetList = []
        for y in ip:
            ipList.append(y.split(' ')[5].split('/')[0])
            subnetList.append(y.split(' ')[5].split('/')[1])
        ip = ipList
        ipList = []
        return ip, subnetList

    def startMenu(self):
        os.system("clear")
        while True:
            try:
                try:
                    data = int(input("""1.) Wifi network reconCore 
2.) BlueTooth reconCore
3.) bluetooth LE reconCore
4.) View previous logs
0.) to exit
[Welcome to SuperSploit Network reconCore mode]: """))
                    return data
                except ValueError:
                    continue
            except KeyboardInterrupt:
                return

    def startChoice(self):
        info = self.getMyInfo()
        os.system("clear")
        try:
            data = int(self.INPUT)
        except TypeError:
            return False
        func = ["return", WifiScan, bt]
        if data == 0:
            return False

        # development lock for not implemented features
        if data > 2:
            input("Sorry not implemented yet press enter to continue")
            return True

        func[data](info)
        self.resetFlags()
        return True

    def resetFlags(self):
        self.INPUT = None
