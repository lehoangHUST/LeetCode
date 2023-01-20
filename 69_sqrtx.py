import math
class Solution:
    # https://androidcalculator.com/how-does-a-calculator-computes-square-roots/?fbclid=IwAR1eQzsbig-ygtCTfUhp4nUpboIatjC3Tj4fxDhD9kRKXi3hw0sj3r7uZOY
    # Link use iterative method or newtons method
    def mySqrt(self, x: int) -> int:
        ans = 1.0
        for i in range(20):
            temp = 1/2 * ans + float(x) / ( 2 * ans)
            ans = temp
        
        return math.floor(ans)