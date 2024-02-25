import json
import traceback
from .errors import Error
from .ToStdOut import ToStdout
import sys


class SetV:

    @classmethod
    def SetV(cls, data):
        try:
            if len(data.split(" ")) < 2:
                Error("No arguments supplied for set\n")
                return
            data = data.split(" ")
            with open(".data/data.json") as file:
                variables = json.load(file)
                file.close()
            ToStdout.write(variables)
        except Exception:
            Error(traceback.format_exc())
            return
