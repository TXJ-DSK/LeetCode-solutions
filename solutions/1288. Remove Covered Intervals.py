# O(NlogN) Time, O(1) Space (in place)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        removed = 0
        intervals.sort(key= lambda x: x[1], reverse=True)
        intervals.sort(key= lambda x: x[0])
        maxend = 0
        for interval in intervals:
            if interval[1] <= maxend:
                removed += 1
            maxend = max(maxend, interval[1])
        return len(intervals) - removed
