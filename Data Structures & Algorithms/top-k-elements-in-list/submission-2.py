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

        arr = []
        for num, count in map.items():
            arr.append([count, num])
        arr.sort()

        while len(res)<k:
            res.append(arr.pop()[1])
        return res