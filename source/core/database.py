# global variables
import json
import os.path

global path_to_database
path_to_database = ".data/data.json"


class DatabaseManagment:

    def __init__(self):
        pass

    @classmethod
    def get(cls):
        if os.path.lexists(path_to_database):
            with open(path_to_database) as file:
                data = json.load(file)
                file.close()
            return data

