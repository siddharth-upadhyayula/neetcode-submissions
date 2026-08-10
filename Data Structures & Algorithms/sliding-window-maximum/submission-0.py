class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxi = 0
        result = []
        for i in range(len(nums)-k+1):
            maxi = max(nums[i:k+i])
            result.append(maxi)
        return result