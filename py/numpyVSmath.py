import numpy as np
import math
import time

x1 = np.arange(0, 10000, 0.01)
x2 = x1
t1 = time.process_time()
for i, j in enumerate(x1):
    x1[i] = math.exp(math.sin(j))
t2 = time.process_time()
print("time of math:", t2-t1)

t1 = time.process_time()
x2 = np.exp(np.sin(x2))
t2 = time.process_time()
print("time of numpy:", t2-t1)
