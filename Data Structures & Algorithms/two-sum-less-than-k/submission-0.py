class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        sum = -1
        nums.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            curr = nums[l] + nums[r]
            if curr < k:
                if curr > sum:
                    sum = curr
                l += 1
            else:
                r -= 1
        return sum