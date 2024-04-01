#!/usr/bin/env python3
import os
import subprocess
import traceback

from prompt_toolkit import prompt

try:
    commands = """sudo apt-get install python3-prompt-toolkit -y
sudo apt-get install python3-pyfiglet -y
sudo apt-get install netcat-traditional adb fastboot pip -y
sudo apt-get install tilix""".split("\n")

    command_one = """pip install --break-system-packages pure-python-adb pwn pybluez
bash <( curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install )
sudo mv ./phoneinfoga /usr/local/bin/phoneinfoga""".split('\n')

    with open(".data/.terminals") as file:
        terms = file.read().split("\n")
        file.close()
    programs = os.listdir("/bin")
    term = False
    prompt("[*] The following will attempt to install a terminal program if none are present in bin folder defaults to "
           "Tilix.\nPress enter to continue")

    for x in terms:
        if x in programs:
            term = True

    if not term:
        subprocess.run(commands[3].split(" "))

    for x in commands:
        if commands.index(x) < 3:
            subprocess.run(x.split(" "))

    for x in command_one:
        subprocess.run(x.split(" "))

except Exception as e:
    print(traceback.format_exc())
    print(f"[!] error: [{e}]. Happened during setup script execution. program was not installed properly. Please "
              f"rerun ./setup.py from install location")
