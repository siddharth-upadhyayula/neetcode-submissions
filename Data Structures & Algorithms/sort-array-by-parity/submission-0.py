class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last = 0
        for i in range(len(nums)):
            if nums[i]&1==0:
                nums[last], nums[i] = nums[i], nums[last]
                last += 1

        return nums