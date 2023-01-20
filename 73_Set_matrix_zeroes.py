class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        position_row = []
        position_col = []
        rows = len(matrix)
        cols = len(matrix[0])

        # Find position zeros by (row and col) in matrix
        for row in range(rows):
            if 0 in matrix[row]:
                for col in range(cols):
                    if matrix[row][col] == 0:
                        position_row.append(row)
                        position_col.append(col)

        # Set value to zero
        for row in range(rows):
            for col in range(cols):
                if row in position_row or col in position_col:
                    matrix[row][col] = 0