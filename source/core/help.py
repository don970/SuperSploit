import os
import subprocess
import traceback
from subprocess import PIPE

from .ToStdOut import ToStdout
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from .errors import Error


history = InMemoryHistory()


class Help:
    def __init__(self):
        pass

    @classmethod
    def help(cls, data):
        data = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
        while True:
            a = data.prompt("Help: ")
            if "exit" in a or "back" in a:
                break
            if a in os.listdir(".data/.help"):
                with open(f".data/.help/{a}", "r") as file:
                    ToStdout.write(file.read())
                    file.close()
                data.prompt("Press enter to continue: ")
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
                    data.prompt("Press enter to continue: ")
                    continue
            except Exception:
                Error(traceback.format_exc())
