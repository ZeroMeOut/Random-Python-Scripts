import numpy as np

# arr = np.array([1, 2, 3, 4, 5])  # A 1-D array

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])  # A 2-D array

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])  # A 3-D array

print(arr)
print("Number of dimensions in this arrays is " + str(arr.ndim))  # Checking how many dimensions are in the array
print(arr[2, 4] + "\n")  # Getting an element from any row

# Slicing is weird, I know it's something like [0:2] or [1:4] for 1-D arrays and [0:2, 0] or [0:2, 0:3] is 2-D arrays
# And also step like [::2].. you get the point. but I can't think of and example rn. .astype() can be used to change
# the data type of an array. I don't know how to use it in any dimension higher than 1-D tho

# Here is a list of some useful NumPy functions and methods names ordered in categories. See routines for the full list.

# Array Creation arange, array, copy, empty, empty_like, eye, fromfile, fromfunction,
# identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like

# Conversions ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat

# Manipulations array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit,
# hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes,
# take, transpose, vsplit, vstack

# Questions all, any, nonzero, where

# Ordering argmax, argmin, argsort, max, min, ptp, searchsorted, sort

# Operations choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask,
# real, sum

# Basic Statistics cov, mean, std, var

# Basic Linear Algebra cross, dot, outer, linalg.svd, vdot
