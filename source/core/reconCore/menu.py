import traceback
from subprocess import Popen, run, PIPE
from ..errors import Error
from ..help import Help
from ..ToStdOut import ToStdout
from .networkRecon import WifiScan
from .Bluetooth import bt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
history = FileHistory('.data/.history/history')
input = PromptSession(history=history, auto_suggest=AutoSuggestFromHistory(), enable_history_search=True)
input = input.prompt


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
                    functions[inputs.index(data)](data)
                    continue
                try:
                    if "clear" in data:
                        ToStdout.write("\033[H\033[J")
                        continue
                    else:
                        cmd = Popen(data.split(" "), stdout=PIPE, stdin=PIPE, stderr=PIPE)
                        output = cmd.communicate()[0], cmd.communicate()[1]
                        for x in output:
                            if len(x) > 0:
                                ToStdout.write(x.decode())
                        continue
                except Exception:
                    Error(traceback.format_exc())
            except Exception:
                Error(traceback.format_exc())
