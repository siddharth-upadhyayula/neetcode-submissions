class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0

        farthest = 0
        cur_end=0
        count=0

        for i in range(len(nums)):

            farthest = max(farthest, i+nums[i])

            if i==cur_end:
                count+=1
                cur_end = farthest

                if cur_end>=len(nums)-1:
                    break
        return count 