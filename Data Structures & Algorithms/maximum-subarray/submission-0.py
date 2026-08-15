class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        arr = []

        maxsum = 0
        curr = 0

        l = 0
        r = 0

        while r<len(nums):
            curr += nums[r]
            if curr<0:
                curr=0
            maxsum = max(curr, maxsum)
            r+=1
        return maxsum

