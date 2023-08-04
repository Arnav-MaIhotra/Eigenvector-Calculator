import linalg
import numpy as np

mat = np.array([[3, 1, 0], [0, 2, 0], [1, 0, 4]])

eig = linalg.eigenvector(mat)

print(eig.eigenvalues)
print(eig.eigenvectors)