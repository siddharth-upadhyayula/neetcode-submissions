"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        current = intervals[0]
        for next_interval in intervals[1:]:
            if current.end > next_interval.start:
                return False
            else:
                current = next_interval

        return True