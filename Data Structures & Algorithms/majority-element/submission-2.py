class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = Counter(nums)
        for i in map:
            if map[i]>len(nums)/2:
                return i 
