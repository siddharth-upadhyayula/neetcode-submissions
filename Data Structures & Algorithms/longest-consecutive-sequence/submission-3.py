class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for i in numset:
            if nums[i]-1 not in nums:
                length = 1

            while length+nums[i] in numset:
                length+=1

            res = max(res, length)
        return res