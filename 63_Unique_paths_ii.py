import numpy as np
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        # Init matrix ones

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        else:
            obstacleGrid = np.array(obstacleGrid)
            # Check condition rows
            for row in range(rows):
                if obstacleGrid[row][0] == 0:
                    obstacleGrid[row][0] = 1
                else:
                    obstacleGrid[row:, 0] = 0
                    break
            
            # Check condition cols
            for col in range(1, cols):
                if obstacleGrid[0][col] == 0:
                    obstacleGrid[0][col] = 1
                else:
                    obstacleGrid[0, col:] = 0
                    break

            # Calculate step
            for row in range(1, rows):
                for col in range(1, cols):
                    if obstacleGrid[row][col] == 1:
                        obstacleGrid[row][col] = 0
                    else:
                        obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
                    print(obstacleGrid)
            return obstacleGrid[rows - 1][cols - 1]

            print(obstacleGrid)

            return 0