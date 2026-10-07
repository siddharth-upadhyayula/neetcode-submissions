class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixsum = {0:1}
        currentsum = 0
        count = 0

        for i in range(len(nums)):

            currentsum+=nums[i]
            needed = currentsum-k

            if needed in prefixsum:
                count+=prefixsum[needed]

            if currentsum in prefixsum:
                prefixsum[currentsum]+=1
            else:
                prefixsum[currentsum]=1

        return count