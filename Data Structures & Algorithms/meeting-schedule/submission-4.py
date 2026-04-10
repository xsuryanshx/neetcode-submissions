"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals = list([i[0],i[1]] for i in intervals)
        if len(intervals)<=1:
            return True
        intervals.sort(key=lambda x:x.start)
        prev = intervals[0]
        for ele in intervals[1:]:
            if ele.start<prev.end:
                return False
            else:
                prev = Interval(min(prev.start, ele.start),max(ele.end,prev.end))
        return True
