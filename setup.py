import getpass
import os
from subprocess import run, Popen, PIPE

installation = f'{os.getenv("HOME")}/.SuperSploit'

try:
    run(["pkexec", "apt-get", "install", "netcat-traditional",  "adb", "fastboot", "pip", "python3-pyfiglet", "python3-prompt-toolkit", "-y"])
except OSError:
    psswd = getpass.getpass("Please enter sudo password: ") + "\n"
    proc = Popen(["sudo", "-S", "apt-get", "install", "netcat-traditional", "adb", "fastboot", "pip", "python3-pyfiglet", "python3-prompt-toolkit", "-y"], stdin=PIPE)
    proc.communicate(psswd.encode())
    
def MakeCFile():
    content = """#include <stdio.h>
int main(){
    system('python3 ')
}"""