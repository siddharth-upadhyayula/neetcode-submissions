class Solution: 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        if len(intervals)==0:
            return []
        
        res = []
        if len(intervals)==1:
            return intervals
        
        current = intervals[0]
        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            if current[1] >= next_interval[0]:
                current = [current[0], max(current[1], next_interval[1])]
            else:
                res.append(current)
                current = next_interval
        
        res.append(current)
        return res