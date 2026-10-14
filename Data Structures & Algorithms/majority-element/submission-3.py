class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1

        for key, val in count.items():
            if val>len(nums)/2:
                return key