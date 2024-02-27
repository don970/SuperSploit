import os
from prompt_toolkit import prompt
from .ToStdOut import ToStdout
input = prompt


class Search:
    def __init__(self):
        pass

    @classmethod
    def search(cls, data):
        data = data.split(" ")
        if len(data) < 2:
            ToStdout.write("please provide a argument to search for")
            return
        key = {}
        exploits = []
        searches = data[2:]
        found = []
        if data[1] == "exploits":
            for x in os.listdir("exploits"):
                for y in os.listdir(f"exploits/{x}"):
                    exploits.append(f"exploits/{x}/{y}")
            if len(data) < 3:
                for i in exploits:
                    print(f'{exploits.index(i)}: {i}')
            for z in exploits:
              for s in searches:
                  if s in z:
                     found.append(z)
            for xx in found:
                print(f'{exploits.index(xx)}: {xx}')
        if data[1] == "payloads":
            for x in os.listdir("payloads"):
                for y in os.listdir(f"payloads/{x}"):
                    exploits.append(f"payloads/{x}/{y}")
            if len(data) < 3:
                for i in exploits:
                    print(f'{exploits.index(i)}: {i}')
            for z in exploits:
              for s in searches:
                  if s in z:
                     found.append(z)
            for xx in found:
                print(f'{exploits.index(xx)}: {xx}')


