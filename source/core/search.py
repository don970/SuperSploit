import os
from prompt_toolkit import prompt
input = prompt


class Search:
    def __init__(self):
        pass

    @classmethod
    def search(cls, data):
        data = data.split(" ")
        key = {}
        exploits = []
        searches = data[2:]
        found = []
        if data[1] == "exploits":
            for x in os.listdir("exploits"):
                for y in os.listdir(f"exploits/{x}"):
                    exploits.append(f"exploits/{x}/{y}")
            for z in exploits:
              for s in searches:
                  if s in z:
                     found.append(z)
            for xx in found:
                print(f'{exploits.index(xx)}: {xx}')
            input("Press enter to continue: ")
        if data[1] == "payloads":
            for x in os.listdir("payloads"):
                for y in os.listdir(f"payloads/{x}"):
                    exploits.append(f"payloads/{x}/{y}")
            for z in exploits:
              for s in searches:
                  if s in z:
                     found.append(z)
            for xx in found:
                print(f'{exploits.index(xx)}: {xx}')
            input("Press enter to continue: ")


