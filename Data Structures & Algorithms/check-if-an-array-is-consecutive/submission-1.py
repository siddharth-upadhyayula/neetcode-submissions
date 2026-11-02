class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(nums)>len(numset):
            return False
        i = 0
        m = min(nums)
        while i<len(nums):
            if m+i not in numset:
                return False
            i+=1
        return True