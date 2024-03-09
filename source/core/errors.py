from .ToStdOut import ToStdout
write = ToStdout.write


class Error:
    def __init__(self, data):
        try:
            if "str" not in str(type(data)):
                data = f"{str(data)}"
            if not data.endswith("\n"):
                data = f"{data}\n"
            with open(".data/.errors/error.log", "a") as stdout:
                stdout.write(data)
                stdout.close()
            write("A error has occurred. and has been logged")
            return
        except Exception as e:
            write(e)
