class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        curr = 0
        i = 0
        if len(nums) == 1:
            return True
        max_reach = 0
        while i < len(nums) and i <= max_reach:
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
            i += 1
        return False