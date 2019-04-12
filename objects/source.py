import numpy as np
from gym_factory.objects import Resource

class Source(Resource):

    def __init__(self, name=None):
        Resource.__init__(self, name, None)


def source():
    return Source()