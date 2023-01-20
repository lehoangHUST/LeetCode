import numpy as np
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # L?y s? lu?ng hàng và c?t
        n = len(matrix)
        rotate_matrix = copy.deepcopy(matrix)
        kernel = np.array([[0,1], [-1,0]])

        for i in range(n):
            for j in range(n):
                position_old = np.array([i, j])
                position_new = np.dot(kernel, position_old)
                i_new, j_new = position_new
                matrix[i_new][j_new + n - 1] = rotate_matrix[i][j]
        return matrix