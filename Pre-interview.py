import numpy as np

data = [int(x) for x in input('data = ').split()]
print(data)
shape = [int(x) for x in input('shape = ').split()]
print(shape)
a = np.reshape(data,(shape[0],shape[1]))
b = a.tolist()
print(b)