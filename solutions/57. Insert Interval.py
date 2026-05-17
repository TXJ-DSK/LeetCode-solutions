# O(N) time, O(N) space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        result = [newInterval]
        for interval in intervals:
            start, end = interval[0], interval[1]
            # two non-merging situations
            if end < result[-1][0]:
                result.insert(len(result)-1, [start, end])
                continue
            if start > result[-1][1]:
                result.append([start, end])
                continue
            # merging
            result[-1][0] = min(start, result[-1][0])
            result[-1][1] = max(end, result[-1][1])
        return result
