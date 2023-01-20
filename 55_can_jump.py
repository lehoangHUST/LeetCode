"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        if n == 1:
            return True

        if 0 not in nums:
            return True
        else:
            
            # Get position have value is 0
            position_zeros = []
            for idx, num in enumerate(nums):
                if num == 0 and idx != n - 1:
                    position_zeros.append(idx)
            if len(position_zeros) == 0:
                return True
            else:

                # Remove index close by unit 1
                i = 1
                while i < len(position_zeros):
                    if (position_zeros[i] - position_zeros[i - 1]) == 1:
                        position_zeros.pop(i - 1)
                    else:
                        i += 1

                print(position_zeros)
                for i, position_zero in enumerate(position_zeros):
                    can_jump = False
                    if i == 0:
                        for j in range(0, position_zero):
                            if nums[j] + j > position_zero:
                                can_jump = True
                    else:
                        for j in range(position_zeros[i - 1] + 1, position_zeros[i]):
                            print(nums[j] + j)
                            if nums[j] + j > position_zero:
                                can_jump = True

                    print(can_jump, i)
                    if can_jump == False:
                        return False
                return True
            """

class Solution:     
 

    def canJump(self, n: list[int]) -> bool:
        
        if 0 not in n[:-1] or len(n) == 1: return True

        pt = n.index(0)            

        for i in range(len(n)):

            if i <= pt and  i + n[i] > pt: pt = i + n[i]

            if i == pt and not n[i]: return False
            if pt >= len(n)-1      : return True

        return True
