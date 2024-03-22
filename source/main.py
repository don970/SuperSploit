import json
import os
from core.inputHandler import Input

# create alliases file
a = {
    "~": os.getenv("HOME")
}

installlocation = f'{os.getenv("HOME")}/.SuperSploit'

with open(f"{installlocation}/.data/Aliases.json", "r") as file:
    di = json.load(file)
    file.close()

if os.getenv("HOME") == di["~"]:
    pass
else:
    with open(f"{installlocation}/.data/Aliases.json", "w") as file:
        file.write(json.dumps(a))
        file.close()


class Main:
    def __init__(self):
        Input.get()
        pass


Main()
