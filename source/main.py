import json
import os
from core.inputHandler import Input

# create an object to hold the aliases

a = {
    "~": os.getenv("HOME"),
    "install_dir": f"{os.getenv('HOME')}/.SuperSploit"
}

# Creating a global variable for the installation path also creates a pointer
# allowing us to use the cd command while still knowing the full path to the
# installation dictionary.

installation = f'{os.getenv("HOME")}/.SuperSploit'


# load aliases globally
with open(f"{installation}/.data/Aliases.json", "r") as file:
    di = json.load(file)
    file.close()

if os.getenv("HOME") == di["~"]:
    pass
else:
    with open(f"{installation}/.data/Aliases.json", "w") as file:
        file.write(json.dumps(a))
        file.close()


class Main:
    def __init__(self):
        """calls the main input handler"""
        Input.get()
        pass


Main()
