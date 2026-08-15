class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        r = len(nums)-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[l] and nums[mid]>nums[r]:
                l=mid
            elif nums[mid]<nums[r] and nums[mid]<nums[l]:
                return nums[mid]
            elif nums[l]<nums[mid] and nums[l]<nums[r]:
                return nums[l]
            else:
                return nums[mid]
            
            

            
