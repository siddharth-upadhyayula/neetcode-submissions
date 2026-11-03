class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        largest = -1
        for val, freq in Counter(nums).items():
            if val>largest and freq==1:
                largest=val
            
        if largest==-1:
            return -1
        return largest