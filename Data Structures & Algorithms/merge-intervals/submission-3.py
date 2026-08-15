class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals)==0:
            return [[]]
        l = 0
        r = 1
        res = []
        if len(intervals)==1:
            return intervals
        
        while l<r and r<len(intervals):
            if intervals[l][1]<intervals[r][0]:
                interval = intervals[l]
                res.append(interval)
                l+=1

            if intervals[l][1]>=intervals[r][0]:
                interval = [min(intervals[l][0],intervals[r][0]), max(intervals[l][1],intervals[r][1])]
                res.append(interval)
                l = r
            
            r+=1

        return res