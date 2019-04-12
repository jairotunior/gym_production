import numpy as np
from abc import ABC


class Resource(ABC):

    def __init__(self, name=None, input = None):
        if name is None:
            self.name = Resource.__name__
        else:
            self.name = name
        self.input = input

    def _process(self):
        pass
