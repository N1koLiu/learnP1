import numpy as np
from scipy import linalg

aArray = np.array([[1, 2], [3, 4]])

print(aArray)

a = linalg.det(aArray)

print(a)

c = np.arange(1, 5, dtype=np.float64)
print(np.power(c, 2).sum())
print(np.add(c, np.arange(4)))