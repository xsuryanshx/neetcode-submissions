class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prevend = intervals[0][1]
        res = 0
        for ele in intervals[1:]:
            if ele[0]<prevend:
                prevend = min(ele[1],prevend)
                res+=1
            else:
                prevend = ele[1]
        return res

