import json
import os
import pty
import traceback
from subprocess import Popen, run, PIPE
from ..errors import Error
from ..help import Help
from ..ToStdOut import ToStdout
from .networkRecon import WifiScan
from .Bluetooth import bt

# redefine input method
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


def sys_call_Linux(data):
    dataList = data.split(' ')
    with open(".data/Aliases.json") as file:
        Aliases = json.load(file)
        file.close()
    for k, v in Aliases.items():
        if k in dataList:
            dataList[dataList.index(k)] = v

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

class menu:


    def __init__(self):

        while True:
            try:
                functions = [WifiScan, bt, Help.recon]
                inputs = ["wifi", "bt", "help"]
                data = input("[Recon menu]: ")
                if "exit" in data:
                    break
                if data in inputs:
                    functions[inputs.index(data)](Error)
                    continue
                try:
                    sys_call_Linux(data)
                except Exception:
                    Error(traceback.format_exc())
            except Exception:
                Error(traceback.format_exc())
