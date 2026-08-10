class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        map = Counter(nums)
        for i in map:
            if map[i]>(len(nums)/3):
                res.append(i)
        return res