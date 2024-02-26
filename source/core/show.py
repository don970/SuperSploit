from .database import DatabaseManagment
from .ToStdOut import ToStdout
class Show:

    @staticmethod
    def show(data):
        if len(data.split(' ')) > 1:
            for x in data.split(" "):
                if data.split(" ").index(x) > 0:
                    for k, v in DatabaseManagment.get().items():
                        if data.split(' ')[data.split(" ").index(x)] == k:
                            ToStdout.write(f"{k}: {v}")
            return

        for k, v in DatabaseManagment.get().items():
            ToStdout.write(f"{k}: {v}")
        return
