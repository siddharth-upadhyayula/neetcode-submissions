class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largest = 0
        for val, freq in Counter(nums).items():
            if val>largest and freq==1:
                largest=val
            
        if largest==0:
            return -1
        return largest