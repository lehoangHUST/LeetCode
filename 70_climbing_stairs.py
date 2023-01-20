import math

class Solution:
    def climbStairs(self, n: int) -> int:
        count = (n // 2) + 1 if n % 2 == 1 else n // 2
        sum = 1 if n % 2 == 0 else 0
        for i in range(count):
            sum += math.comb(n-i, n - i*2)
        return sum