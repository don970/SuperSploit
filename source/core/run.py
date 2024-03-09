import os
import subprocess
from .database import DatabaseManagment
from prompt_toolkit import prompt
from .help import Help
from .ToStdOut import ToStdout


class Genrate_payload:
    def __init__(self, data):
        self.db = data
        return


    def compileForAndroid(self, *args):
        cwd = os.getcwd()
        try:
            os.mkdir(f"{os.getenv('HOME')}/.android_payload")
        except FileExistsError:
            pass
        if "exploits/android" in os.getcwd():
            ToStdout.write("Starting android app generator. ")
            compileCmd = subprocess.run(["buildozer", "android", "debug"], capture_output=True)
            if "Android packaging done!" in compileCmd.stdout.decode():
                ToStdout.write("APK myapp-0.1-arm64-v8a_armeabi-v7a-debug.apk available in the bin directory")
                return True
            else:
                ToStdout.write(compileCmd.stdout.decode())
        return


class run:

    def __init__(self, *args):
        while True:
            funcs = (Help.help, Genrate_payload.compileForAndroid)
            inputs = ("help", "android")
            self.database = DatabaseManagment.get()
            Genrate_payload(self.database)
            data = prompt("[Payload Generator]: ")
            if "exit" in data:
                break
            if data in inputs:
                funcs[inputs.index(data)](data)
