import numpy as np
import matplotlib

def getWhiteningMatrix(X):
    #X is a matrix
    sigma = np.cov(X, rowvar = True)
    U,S,V = np.linalg.svd(sigma)
    # U - eigenvectors
    # S - eigenvalues
    # V - transpose
    epsilon = 1e-5
    whitenedMatrix = np.dot(U, np.dot(np.diag(1.0 / np.sqrt(S + epsilon)), U.T))
    return whitenedMatrix

X = np.array([[0, 2, 2], [1, 1, 0], [2, 0, 1], [1, 3, 5], [10, 10, 10] ]) # Input: X [5 x 3] matrix
ZCAMatrix = getWhiteningMatrix(X) # get ZCAMatrix
xZCAMatrix = np.dot(ZCAMatrix, X) # project X onto the ZCAMatrix