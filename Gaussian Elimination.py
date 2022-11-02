# For n = 2, 3,...generate the Hilbert matrix of order n, and also generate the n-vector b = Hx, where x is the n-vector
# with all of its components equal to 1. Use a Python library routine for Gaussian Elimination to solve the resulting
# linear system Hx = b, obtaining an approximate solution x hat. Compute the infinite-norm of the residual r = b - H * xhat
# and of the error delta x = xhat - x, where x is the vector of all ones. How large can you take n before the error is
# 100 percent?

import numpy as np

# choose some order for the Hilbert matrix
n = 5

# Create an array H with starting values of 0
H = np.zeros((n,n))

# Generate entries for each respective ith row and jth column value using the given rule hij
for i in range(n):
    for j in range(n):
        H[i, j] = 1.0 / (i + j + 1)
print("H =")
print(H, "\n")

# Create an array where x is the n-vector with all of its components equal to 1
x = np.zeros((n, 1))
for i in range(n):
    for j in range(1):
        x[i, j] = 1.0
print ("x =")
print(x, "\n")

# Multiply the matrices H and x to determine b
b = np.dot(H, x)
print("b =")
print(b, "\n")

# Determine the upper and lower triangular matrices of H via Gaussian Elimination to perform the LU factorization
U = np.triu(H) 
L = np.tril(H)
print ("U =")
print(U, "\n")
print("L =")
print(L, "\n")

# the solution obtained from solving Hx = b and call it x_hat
x_hat = b

# result obtained from multiplying H and x_hat
b_hat = np.dot(H, x_hat)

# Calculate and store the result of the residual here
r = b - b_hat
print("r =")
print(r, "\n")

# Calculate and store the result of the error here
error = x_hat - x
print("error =")
print(error, "\n")

# Calculate and store the results of the infinite norm for the residual here
r_infinite_norm = max(np.sum(abs(r), axis = 1))
print("infinite norm of residual =", r_infinite_norm)

# Calculate and store the results of the infinite norm for the error here 
error_infinite_norm = max(np.sum(abs(error), axis = 1))
print("infinite norm of error =", error_infinite_norm)

