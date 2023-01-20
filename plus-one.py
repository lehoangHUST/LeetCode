class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 1
        for idx, digit in enumerate(digits):
            number += digit * (10**(len(digits) - 1 - idx))
        
        new_digits = []

        while number != 0:
            new_digits.append(number % 10)
            number //= 10
        
        return new_digits[::-1]