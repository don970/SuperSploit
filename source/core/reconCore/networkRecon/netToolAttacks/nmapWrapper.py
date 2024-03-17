# This is a wrapper for nmap
import os
from subprocess import run


class nmap:
    def __init__(self, ip):
        """This is a wrapper to use the tool nmap to
        scan for live host identification and more"""
        self.ip = ip[0]
        self.ipStr = ''
        iplist = self.ip[0].split(".")
        n = 0
        while n <= 2:
            if n == 0:
                self.ipStr += iplist[n]
                n += 1
                continue
            self.ipStr += '.' + iplist[n]
            n += 1
        self.ipStr += f""".0/{ip[1][0]}"""
        self.basicScan()
        return

    def basicScan(self) -> None:
        if not input(f"would you like to perform a scan with a subnet of ({self.ipStr}): ").startswith("y"):
            return
        print("scanning")
        a = run(["nmap", "-sn", self.ipStr], capture_output=True)
        li = []
        result = a.stdout.decode().split('\n')
        self.results = result
        for x in result:
            if len(x) > len("scan report for xxx.xxx.xxx.xxx"):
                li.append(x.split(" ")[4])
        os.system("clear")
        for x in li:
            if x == "addresses" or "http" in x:
                continue
            print(x)
        with open("Notes/IpCaptures", "a") as file:
            file.write(f"\n\n host = {li[0]}")
            for x in li:
                file.write(f"\n{x}\n")
            file.close()
        input("Full capture logged in Notes folder. press enter to continue")
        # add a way to dump the ips
        return
