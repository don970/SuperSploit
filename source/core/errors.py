
class Error:
    def __init__(self, data):
        if "str" not in str(type(data)):
            data = f"{str(data)}"
        if not data.endswith("\n"):
            data = f"{data}\n"
        with open("/dev/stdout", "w") as stdout:
            stdout.write(data)
            stdout.close()
        return

