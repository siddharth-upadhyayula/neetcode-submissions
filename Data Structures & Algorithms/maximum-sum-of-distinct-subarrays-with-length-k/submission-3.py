class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        current=0
        freq = {}
        for r in range(len(nums)):
            current+=nums[r]
            freq[nums[r]]=freq.get(nums[r],0)+1
            if r-l+1==k:
                if len(freq)==k:
                    count = max(current,count)
                current-=nums[l]
                freq[nums[l]]-=1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l+=1

        return count