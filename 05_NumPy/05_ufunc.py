import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
# z = np.divmod(y,x)
# print(z)

# arr = np.array([3.2, 3.6])
# print(np.trunc(arr)) # Will trunc to near ZERO
# print(np.fix(arr)) # Will fix element towards Zero
# print(np.round(arr)) # Will round up the value
# print(np.floor(arr)) # Will take value towards below integer
# print(np.ceil(arr)) # Will take next integer

# print(np.prod([x, y]))


arr = np.arange(1,11)
print(np.lcm.reduce(arr))