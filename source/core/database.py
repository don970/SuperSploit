# global variables
import json

global path_to_database
path_to_database = ".data/data.json"


class DatabaseManagment:

    def __init__(self):
        pass

    @classmethod
    def get(cls):
        with open(path_to_database) as file:
            data = json.load(file)
            file.close()
        return data

