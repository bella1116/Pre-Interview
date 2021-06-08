class Tensor():

    def __init__(self, data, shape):
        self.data = [int(x) for x in input('data = ').split()]
        self.shape = [int(x) for x in input('shape = ').split()]
        self.tensor = Tensor(data, shape)

    def Data(self, data):
        self.data = data


    def Shape(self, shape):
        self.shape = shape
        