import os
import subprocess
import traceback
from subprocess import PIPE

from .ToStdOut import ToStdout
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit import prompt
from .errors import Error


history = InMemoryHistory()

class Help:
    def __init__(self):
        pass

    @classmethod
    def help(cls, data):
        data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
        while True:
            ToStdout.write('all - shows basic help page')
            a = data.prompt("Help: ")
            if "exit" in a or "back" in a:
                break
            if a in os.listdir(".data/.help"):
                with open(f".data/.help/{a}", "r") as file:
                    ToStdout.write(file.read())
                    file.close()
                continue
            try:
                if "clear" in a:
                    ToStdout.write("\033[H\033[J")
                else:
                    cmd = subprocess.Popen(a.split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE)
                    output = cmd.communicate()[0], cmd.communicate()[1]
                    for x in output:
                        if len(x) > 0:
                            ToStdout.write(x.decode())
                    continue
            except Exception:
                Error(traceback.format_exc())

