class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for i in range(len(nums)):
            if nums[i] in nums:
                length = 1

            while length+nums[i] in numset:
                length+=1

            res = max(res, length)
        return res