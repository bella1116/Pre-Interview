import numpy as np

class Tensor():
    data = [int(x) for x in input('data = ').split()]
    print(data)
    shape = [int(x) for x in input('shape = ').split()]
    print(shape)
    a = np.reshape(data, (shape[0], shape[1]))
    b = a.tolist()
    print(b)

    def __init__(self, data, shape, output):
        self.data = data
        self.shape = shape
        self.tensor = Tensor(data,shape)

    def Reshape(self):
        if len(self.data) == 0:
            print('[]')
        if len(self.shape) == 0:
            print('[]')
