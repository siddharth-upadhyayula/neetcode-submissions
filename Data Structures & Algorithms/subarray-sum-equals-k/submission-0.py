class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        prefix = {0:1}
        count = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            needed = prefix_sum - k

            if needed in prefix:
                count += prefix[needed]

            if prefix_sum in prefix:
                prefix[prefix_sum] += 1
            else:
                prefix[prefix_sum] = 1

        return count
