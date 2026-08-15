class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for i in numset:
            if i-1 not in nums:
                length = 1

            while length+i in numset:
                length+=1

            res = max(res, length)
        return res