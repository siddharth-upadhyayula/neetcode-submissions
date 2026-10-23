class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res=[]
        curr=[]
        def dfs(start, candidates, target):

            if target==0:
                res.append(curr.copy())
                return

            if target<0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break

                curr.append(candidates[i])
                dfs(i+1, candidates, target - candidates[i])
                curr.pop()

        dfs(0, candidates, target)
        return res