import numpy as np

""" Create a basic array """
# create a simply array by passing a list to it
a = np.array([1, 2, 3])

# create an array filled with 0's
a = np.zeros(2)     # two 0's

# create an array filled with 1's
a = np.ones(2)     # two 1's

# create an array whose initial content is random and depends on the state of the memory
a = np.empty(2)

# create an array with a range of elements
a = np.arange(4)     # a is np.array([0, 1, 2, 3])

# create an array that contains a range of evenly spaced interval. 
# The first number, last number, and the step size shoud be specified.
a = np.arange(2, 9, 2)     # a is np.array([2, 4, 6, 8])

# create an array with values that are spaced linearly in a specified interval
a = np.linspace(0, 10, num=5)     # a is np.array([0, 2.5, 5, 7.5, 10])

# specify a date type using the /dtype/ keyword. 
#~the default data type is floating point(np.float64)
a = np.ones(2, dtype=np.int64)

""" Adding, removing, and sorting elements """
# Get a sorted copy of an array
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
sorted_arr = np.sort(arr)

# Concatenate arrays
# Case 1
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
ab = np.concatenate((a, b))
# Case 2
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
xy = np.concatenate((x, y), axis=0)

""" The shape and size of an array """
array_example = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0 ,1 ,2, 3], [4, 5, 6, 7]]])

# ndarray.ndim will tell you the number of axes, or dimensions, of the array.
array_dimension = array_example.ndim
# ndarray.size will tell you the total number of elements of the array.
#~This is the product of the elements of the array’s shape.
array_size = array_example.size
# ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array.
#~If, for example, you have a 2-D array with 2 rows and 3 columns,
#~the shape of your array is (2, 3).
array_shape = array_example.shape

""" Reshape an array """
a = np.arange(6)
b = a.reshape(3, 2)     # b is [[0 1] [2 3] [4 5]]
c = np.reshape(a, newshape=(1, 6), order='C')     # Attention! This is different from a.reshape
# /newshape/ is an integer or a tuple of integers.
