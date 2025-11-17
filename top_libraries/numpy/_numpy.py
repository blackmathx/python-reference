'''
NumPy is the foundation of the Python Machine Learning stack. NymPy is a library adding 
support for large, multi-dimensional arrays and matrices, along with high-level math 
functions to operate on these arrays.

https://numpy.org

'''

import numpy as np

# vector
vec = np.array([1, 3, 4, 4, 3, -1])
print(vec[0])


# matrix
mtrx = np.array([[1, 2, 3],
                 [2, 3, 4],
                 [1, 3, 2]])
print(mtrx.shape)
print(mtrx.ndim)
print(np.mean(mtrx, axis=0))
print(mtrx.T) 
print(mtrx[1, 2]) # 4 # zero-indexed row-col selection, same as vectors 

# numpy's linalg library
rank = np.linalg.matrix_rank(mtrx)
det = np.linalg.det(mtrx)
print('rank: ' + str(rank))
print('det: ' + str(det))

# numpy dot product
vec1 = np.array([2, 3, 4])
vec2 = np.array([1, 2, 1])
print('dot product: ' + str(np.dot(vec1, vec2)))  # use dot to multiply matrices

# random numbers
a = np.random.random()
b = np.random.random(2) # random array  of len 2
c = np.random.randint(0, 11, 3) # 3 random numbers in [1, 10]
d =  np.random.seed(99) # setting a seed will produce the same output
