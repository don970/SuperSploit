"""
1.) show connected devices
2.) show individual device info
3.) use traceroute to scan for more networks
4.) use nmap to scan a network
5.) use custom script
0.) back
"""

from .netToolAttacks import nmap

class __WIRELESS__:
    def __init__(self, ip):
        self.data = None
        self.INITIALIZED = None
        self.functions = [nmap]
        self.listOfData = [1, 2, 3, 4, 5, 6]
        self.myIp = ip
        self.main(ip)

    def trigger(self):
        """This is what checks and displays the info"""
        if self.data == 0:
            return
        if not self.INITIALIZED:
            return
        try:
            if self.data in self.listOfData:
                if self.myIp is None:
                    return "Error setting the ip"
                self.functions[self.listOfData.index(self.data)](self.myIp)
        except ValueError:
            return



    def main(self, data):
        """We are going to use the main method as a standalone call and trigger for basic network reconCore"""
        self.INITIALIZED = True
        self.data = data
        self.trigger()
        pass

