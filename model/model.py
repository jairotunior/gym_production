import numpy as np
from gym_factory.objects import Resource

from collections import deque

class Model:

    def __init__(self, name=None, description=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

        self.objects = deque()
        self.compiled_model = False

    def add(self, resource: Resource):
        self.objects.append(resource)
        if len(self.objects) > 1:
            self.objects[-1].input = self.objects[-2]