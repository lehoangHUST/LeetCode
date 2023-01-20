class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        i = 0
        for num in nums:
            i += num
            sums.append(i)
        return sums