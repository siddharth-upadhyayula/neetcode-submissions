class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        maxi = 0
        res = []
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1

        for i in range(k):
            maxi = max(map)
            res.append(maxi)
            del map[maxi]

        return res