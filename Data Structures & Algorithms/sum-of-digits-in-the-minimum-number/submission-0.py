class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        total = 0
        for i in str(min(nums)):
            total+=int(i)
        if (total%2)==0:
            return 1
        return 0