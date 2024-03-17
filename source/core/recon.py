from .database import DatabaseManagment
from .reconCore import menu

class Recon:

    def __init__(self, *args):
        while True:
            print(1111111111111)
            self.database = DatabaseManagment.get()
            menu()
