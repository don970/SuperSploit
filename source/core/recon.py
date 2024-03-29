import json
import os
import pty
import traceback
import socket
from .errors import Error
from .ToStdOut import ToStdout
from .help import Help
from .show import Show
from .set import SetV
from .exploithandler import ExploitHandler
from .use import use
from .search import Search
from .banners import banners
from .database import DatabaseManagment
from subprocess import Popen, run, PIPE
from .reconCore.networkRecon import WifiScan
from .reconCore.Bluetooth import bt
from .reconCore.external_tools.phoneinfoga import Phone
# redefine input method
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
installation = f'{os.getenv("HOME")}/.SuperSploit'
history = FileHistory(f'{installation}/.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


def recon_ng(data):
    run(["python3", f"{installation}/source/core/reconCore/external_tools/recon-ng/recon-ng"])
    return

def sys_call_Linux(data):
    dataList = data.split(' ')
    with open(".data/Aliases.json") as file:
        Aliases = json.load(file)
        file.close()

    for k, v in Aliases.items():
        if k in dataList:
            dataList[dataList.index(k)] = v

    # Catch cd command being passed
    if "cd" in dataList:
        ToStdout.write("[*] The cd command will spawn a shell in the folder you change to. This is\n"
                       "because the program release on the working dir to be the programs install\n"
                       "folder. I will update in future to be able to just use cd.")
        cwd = os.getcwd()
        os.chdir(dataList[1])
        pty.spawn(f"{os.getenv('SHELL')}")
        os.chdir(cwd)

    # check for cat
    if "cat" in dataList:
        with open(dataList[1], 'r') as file:
            ToStdout.write(file.read())
            file.close()
            return
    try:
        # check for ls
        if "ls" in data:
            cmd = run(dataList)
            return

        cmd = Popen(dataList, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        output = cmd.communicate()[0], cmd.communicate()[1]
        for x in output:
            if len(x) > 0:
                ToStdout.write(x.decode())
        return True

    except Exception:
        return False

def get_network_info():
    host = socket.gethostname()
    data = run(["ip", "addr"], capture_output=True).stdout.decode().split("\n")
    for i in data:
        if "inet" and "brd" in i and ":" not in i:
            ip = i.split(" ")[5].split('/')[0]
            subnet = i.split(" ")[5].split('/')[1]
            return ip, subnet, host

class Recon:

    def __init__(self, args):
        self.database = DatabaseManagment.get()

        while True:
            try:
                functions = [recon_ng, Phone, WifiScan, bt, Help.recon, Help.help, Show.show, SetV.SetV, ExploitHandler, use, Search.search, banners, DatabaseManagment.addVariableToDatabase]
                inputs = ["recon-ng", "phoneinfoga", "wifi", "bt", "recon-help", "help", "show", "set", "exploit", "use", "search", "banner", "add"]
                data = input("[Recon menu]: ")
                if data.split(" ")[0] in inputs:
                    functions[inputs.index(data.split(" ")[0])](data)
                    continue
                if "exit" in data:
                    break
                try:
                    sys_call_Linux(data)
                except Exception:
                    Error(traceback.format_exc())
            except Exception:
                Error(traceback.format_exc())
