class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0 or len(intervals)==1:
            return 0
        intervals = sorted(intervals, key = lambda x:x[1])
        current = intervals[0]
        count = 0

        for next in range(1, len(intervals)):
            if current[1]>intervals[next][0]:
                count+=1
            current = intervals[next]
        return count

            

