import os
import sys
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

history = FileHistory('.data/.history/history')



class Input:
    @classmethod
    def sys_call_Linux(cls, data):
        try:
            if "ls" in data:
                cmd = subprocess.run(["ls", data.split(" ")[1]])
                return
            cmd = subprocess.Popen(data.split(" "), shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            output = cmd.communicate()[0], cmd.communicate()[1]
            for x in output:
                if len(x) > 0:
                    ToStdout.write(x.decode())
            return True
        except Exception as e:
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
        pass

    @classmethod
    def check(cls, data):
        try:
            if data.endswith(" "):
                data = data.lstrip(" ")
            functions = [Help.help, Show.show, SetV.SetV, ExploitHandler, use, Search.search, banners]
            inputs = ["help", "show", "set", "exploit", "use", "search", "banner"]
            if data.split(" ")[0] in inputs:
                functions[inputs.index(data.split(" ")[0])](data)
                return
            if "clear" in data:
                ToStdout.write("\033[H\033[J")
                return
            else:
                if "exit" in data:
                    sys.exit()
                if "Linux" in os.uname():
                    cls.sys_call_Linux(data)
                else:
                    cls.sys_call_other(data)
        except Exception:
            Error(traceback.format_exc())

    @classmethod
    def get(cls):
        while True:
            try:
                data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
                inp = data.prompt("SuperSploit: ")
                cls().check(inp)
            except Exception:
                Error(traceback.format_exc())
                continue
