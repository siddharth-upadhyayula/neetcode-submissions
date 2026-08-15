class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            if nums[i]-1 in nums:
                res+=1
        return res