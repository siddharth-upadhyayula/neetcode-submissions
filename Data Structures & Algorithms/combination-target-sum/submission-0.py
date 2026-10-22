from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start: int, remaining: int, curr: List[int]) -> None:
            if remaining == 0:
                res.append(curr.copy())
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                curr.append(nums[i])
                dfs(i, remaining - nums[i], curr)
                curr.pop()

        dfs(0, target, [])
        return res