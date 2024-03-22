from .database import DatabaseManagment

class use:
    def __init__(self, data):
        data = data.split(" ")
        exploits = DatabaseManagment.getExploits()
        payloads = DatabaseManagment.getPayloads()
        data[2] = int(data[2])
        if data[1] == "exploit":
            DatabaseManagment.directlyModify([data[1], exploits[data[2]]])
        else:
            DatabaseManagment.directlyModify([data[1], payloads[data[2]]])
        pass