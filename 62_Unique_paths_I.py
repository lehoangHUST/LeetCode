import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            + [i][0] or [0][j] is one step
            + steps to dist is: a[i][j] condition (i != 0 and j != 0)
                a[i][j] = step to a[i- 1][j] + step to a[i][j - 1]
                a[i][j] = 1 with i == 0 or j == 0
        """

        matrix_step = np.ones((m, n), dtype=int)
        for i in range(1, m):
            for j in range(1, n):
                matrix_step[i][j] = matrix_step[i - 1][j] + matrix_step[i][j - 1]
        
        return matrix_step[m - 1][n - 1]