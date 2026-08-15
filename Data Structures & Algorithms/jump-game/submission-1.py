class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        i = 0
        sum=0
        if len(nums) == 1:
            return True
        while i<len(nums):
            if nums[i]==0:
                break
            else:
                curr = i+nums[i]
                sum+=nums[i]

            if curr >= len(nums)-1:
                return True

            i = curr
        return False