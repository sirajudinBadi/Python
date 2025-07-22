import numpy as np

"""
NumPy Array Characteristics:
    - Homogenous Data Type.
    - Shape should be rectangular.
    - Once created, Total size of an array cannot be changed.
    - Array is mutable
"""


"""
    Dimesions :
    0-Dimensional = Each value in array is 0_dimensional
    1-Dimensional = An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
    2-Dimensional = An array that has 1D arrays as its elements is called 2D Array.
"""

# How to define

arr_0d = np.array(23)
arr_1d = np.array([1,2,3,4,5,6,7])
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]]) # 2D array
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]], [[13,14,15],[16,17,18]]])
# print(arr_0d.ndim)
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)

# Creation of array by specifying the dimensions
arr_dim = np.array([1,2,3,4], ndmin=5)
# print(arr_dim)

# print(arr_1d[2]+arr_1d[5])
# print(arr_2d[1,1])
# print(arr_3d[2,0,1])

# Slicing
# print(arr_2d[:,1:])

"""
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
"""

# print(arr_2d.dtype)

# str_arr = np.array([1,2,3,4,5], dtype="S")
# print(str_arr)
# print(str_arr.dtype)


arr = np.array([1.1, 2.2, 3.3, 4.4])
# new_arr = arr.astype("i")
# print(new_arr)
# print(new_arr.dtype)

new_arr = arr.copy()
new_view = arr.view()
arr[0] = 4.4
# print(new_view.base) # Holds the array
# print(new_arr.base) # None

# print(arr_3d.shape)

a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,2,-1)
print(b)

# print(arr_3d.reshape(-1))

