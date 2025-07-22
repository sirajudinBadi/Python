import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr_2d = arr.reshape(4,3)
arr_3d = arr.reshape(2,2,3)


# for x in np.nditer(arr_3d):
#     print(x)

# for x in np.nditer(arr_3d,flags=["buffered"], op_dtypes = ["S"]):
#     print(x, end=" ")

# Enumerate in 2D array
# for idx, x in np.ndenumerate(arr_2d):
#     print(idx, x)