from itertools import chain

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vector = list(chain.from_iterable(matrix))
        
        left, right = 0, len(vector) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == vector[mid]:
                return True
            elif target < vector[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False