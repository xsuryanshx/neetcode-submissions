class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        print(intervals)
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



        
            

                

