from gym_factory.objects import Resource

class Processor(Resource):

    def __init__(self, name=None, setup_time: int = 0, process_time: int = 1, capacity: int = 1, input: Resource = None):
        Resource.__init__(self, name, input)

        self.setup_time = setup_time
        self.process_time = process_time
        self.capacity = capacity

    def __call__(self, input: Resource):
        self.input = input


def processor(name=None, setup_time: int = 0, process_time: int = 1, capacity: int = 1):
    def func(input):
        return Processor(name=name, setup_time=setup_time, process_time=process_time, capacity=capacity, input=input)