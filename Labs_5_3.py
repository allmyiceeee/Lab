import numpy as np
a = np.zeros(10, dtype  = np.uint16)
b = np.zeros(10, dtype  = np.uint16)
for i in range(len(b)):
    b[i] = 2
c = np.arange(10, 15, 0.5, dtype = np.float32)

random_array = np.random.default_rng().integers(low=-100, high=100, size=20)
negative_random_array = np.empty(0)
lst1 = []

for c in random_array:
    if c < 0:
        lst1.append(c)

print(np.append(negative_random_array, lst1))

