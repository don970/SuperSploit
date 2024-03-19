import json
import os
from core.inputHandler import Input


print(os.getcwd())
a = {
    "~": os.getenv("HOME")
}
with open(".data/Aliases.json", "w") as file:
    file.write(json.dumps(a))
    file.close()

class Main:
    def __init__(self):
        Input.get()
        pass


Main()
