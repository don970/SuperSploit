from .database import DatabaseManagment
from .reconCore import menu

class Recon:

    def __init__(self, *args):
        self.database = DatabaseManagment.get()
        menu()
