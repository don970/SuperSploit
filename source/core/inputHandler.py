import os
import sys
import traceback

from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import subprocess
from subprocess import PIPE
from .errors import Error
from .ToStdOut import ToStdout
from .help import Help
from .show import Show
from .set import SetV
history = InMemoryHistory()



class Input:

    def __init__(self):
        pass

    @classmethod
    def check(cls, data):
        try:
            functions = [Help.help, Show.show, SetV.SetV]
            inputs = ["help", "show", "set"]
            if data.split(" ")[0] in inputs:
                functions[inputs.index(data.split(" ")[0])](data)
                return
            if "clear" in data:
                ToStdout.write("\033[H\033[J")
                return
            else:
                if "exit" in data:
                    sys.exit()
                cmd = subprocess.Popen(data.split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE)
                output = cmd.communicate()[0], cmd.communicate()[1]
                for x in output:
                    if len(x) > 0:
                        ToStdout.write(x.decode())
                        return
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
