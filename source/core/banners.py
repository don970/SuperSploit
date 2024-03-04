import pyfiglet

from .ToStdOut import ToStdout
import os
import random

class banners:
    def __init__(self, *args):
        with open(f".data/.banners/{random.choice(os.listdir('.data/.banners/'))}") as file:
            data = file.read()
            file.close()
            data = data.split("#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!")
            choice = random.choice(data)
            ToStdout.write(choice)
