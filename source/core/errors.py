from .ToStdOut import ToStdout
write = ToStdout.write


class Error:
    def __init__(self, data):
        try:
            if "str" not in str(type(data)):
                try:
                    data = data.decode()
                    pass
                except Exception:
                    data = f"{str(data)}"
                    pass
            if not data.endswith("\n"):
                data = f"{data}\n"
            with open(".data/.errors/error.log", "a") as stdout:
                stdout.write(data)
                stdout.close()
            write(data)
            return
        except Exception as e:
            write(e)
