import linear_algebra
import numpy as np

mat = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

eig = linear_algebra.eigenvector(mat)

print(eig.eigenvalues)
print(eig.eigenvectors)
