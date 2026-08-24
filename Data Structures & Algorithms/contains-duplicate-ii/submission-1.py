class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        map = {}

        for i in range(len(nums)):

            if nums[i] in map:
                map[nums[i]].append(i)

            else:
                map[nums[i]]=[i]

        for num in map:
            for idx in range(len(map[num]) - 1):
                if abs(map[num][idx] - map[num][idx + 1]) <= k:
                    return True
        return False