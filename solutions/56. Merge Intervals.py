class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        #print(intervals)
        result = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= result[-1][1]:
                result[-1][1] = max(inter[1],result[-1][1])
            else:
                result.append(inter)
        return result
        
