class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = [], [], []
        for num in nums:
            if num == 0:
                red.append(0)
            elif num == 1:
                white.append(1)
            else:
                blue.append(2)
        
        nums[:len(red)] = [0] * len(red)
        nums[len(red):len(red) + len(white)] = [1] * len(white)
        nums[len(red) + len(white):len(red) + len(white) + len(blue)] = [2] * len(blue)