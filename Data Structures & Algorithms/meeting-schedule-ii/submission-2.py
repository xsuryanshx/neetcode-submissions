"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        if len(intervals)<=1:
            return len(intervals)
        
        rooms = []
        rooms.append(intervals[0].end)

        for ele in intervals[1:]:
            used = False
            for i in range(len(rooms)):
                if ele.start >= rooms[i]:
                    rooms[i] = ele.end
                    used = True
                    break
            if not used:
                rooms.append(ele.end)
        print(rooms)
        return len(rooms)
                


                


        