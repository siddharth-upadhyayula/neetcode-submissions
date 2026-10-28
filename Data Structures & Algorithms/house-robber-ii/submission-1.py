class Solution:
    def rob(self, nums: List[int]) -> int:
        res = max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        return res

    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for i in nums:
            newRob = max(rob1 + i, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2