from gym_factory.objects import Resource

class Sink(Resource):

    def __init__(self, name=None, input: Resource = None):
        Resource.__init__(self, name, input)

    def __call__(self, input: Resource):
        self.input = input