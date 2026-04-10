class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final_arr = []
        prev = intervals[0]
        for ele in intervals[1:]:
            if ele[0] <= prev[1]:
                prev = [min(ele[0],prev[0]),max(prev[1],ele[1])]
            else:
                final_arr.append(prev)
                prev = ele
        final_arr.append(prev)

        return final_arr 