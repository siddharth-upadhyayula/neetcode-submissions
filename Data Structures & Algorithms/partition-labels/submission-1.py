class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i,c in enumerate(s):
            last[c]=i

        res = []
        end = 0
        start = 0

        for i,c in enumerate(s):
            end = max(last[c], end)

            if i==end:
                res.append(end-start+1)
                start=i+1

        return res
