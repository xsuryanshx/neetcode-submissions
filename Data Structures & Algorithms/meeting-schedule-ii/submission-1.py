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
            dont_add = 0
            for i in range(len(rooms)):
                if ele.start >= rooms[i]:
                    rooms[i] = ele.end
                    dont_add = 1
                    break
                else:
                    rooms_to_add = ele.end
            if dont_add !=1:
                rooms.append(rooms_to_add)
        print(rooms)
        return len(rooms)
                


                


        