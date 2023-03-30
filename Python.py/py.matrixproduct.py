import numpy as np
  

arr1 = np.array([[1, 2, 3], [4, 5, 6],
                 [7, 8, 9]])
arr2 = np.array([[11, 12, 13], [14, 15, 16],
                 [17, 18, 19]])
  
matrix_product = np.matmul(arr1, arr2)
print("Matrix Product is ")
print(matrix_product)
print()
