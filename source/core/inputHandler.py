import json
import os
import sys
import pty
import traceback
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import subprocess
from subprocess import PIPE
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
from .recon import Recon

installation = f'{os.getenv("HOME")}/.SuperSploit'
history = FileHistory(f'{installation}/.data/.history/history')


env = os.environ
class Input:
    @classmethod
    def sys_call_Linux(cls, data):
        shells = DatabaseManagment.findShells()
        if data in shells:
            subprocess.run([f"/usr/bin/{data}"])
        dataList = data.split(' ')
        with open(f"{installation}/.data/Aliases.json") as file:
            Aliases = json.load(file)
            file.close()
        for k, v in Aliases.items():
            if k in dataList:
                dataList[dataList.index(k)] = v

        if "cd" in dataList:
            os.chdir(dataList[1])
            return

        if "cat" in dataList:
            with open(dataList[1], 'r') as file:
                ToStdout.write(file.read())
                file.close()
                return

        try:
            if "ls" in data:
                cmd = subprocess.run(dataList)
                return
            cmd = subprocess.Popen(dataList, shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            output = cmd.communicate()[0], cmd.communicate()[1]
            for x in output:
                if len(x) > 0:
                    ToStdout.write(x.decode())
            return True
        except Exception:
            Error(traceback.format_exc())
            return False

    @classmethod
    def sys_call_other(cls, data):
        try:
            cmd = subprocess.Popen(data.split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE)
            output = cmd.communicate()[0], cmd.communicate()[1]
            for x in output:
                if len(x) > 0:
                    ToStdout.write(x.decode())
                return True
        except Exception:
            Error(traceback.format_exc())
            return False

    def __init__(self):
        """This handles all the input"""
        pass

    @classmethod
    def check(cls, data):
        try:
            if "exit" in data:
                sys.exit()
            if "clear" in data:
                ToStdout.write("\033[H\033[J")
                return
            if data.endswith(" "):
                data = data.lstrip(" ")
            functions = [Show.shells, Recon, Help.help, Show.show, SetV.SetV, ExploitHandler, use, Search.search, banners, DatabaseManagment.addVariableToDatabase]
            inputs = ["shells", "recon", "help", "show", "set", "exploit", "use", "search", "banner", "add"]
            try:
                if data.split(" ")[0] in inputs:
                    functions[inputs.index(data.split(" ")[0])](data)
                    return
                if "Linux" in os.uname():
                    cls.sys_call_Linux(data)
                    return
                cls.sys_call_other(data)
            except Exception:
                Error(traceback.format_exc())
        except Exception:
            Error(traceback.format_exc())

    @classmethod
    def get(cls):
        banners()
        while True:
            try:
                data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
                inp = data.prompt("SuperSploit: ")
                cls().check(inp)
            except Exception:
                Error(traceback.format_exc())
                continue
