class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        maxsum = float("-inf")
        curr = 0
        r = 0

        while r<len(nums):
            curr += nums[r]
            maxsum = max(curr, maxsum)
            if curr<0:
                curr=0
            r+=1
        return maxsum