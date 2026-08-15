class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in Counter(nums):
            if nums[i]>len(nums)/2:
                return i 
                