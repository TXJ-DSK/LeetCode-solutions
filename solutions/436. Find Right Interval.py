class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            if intervals[0][0] == intervals[0][1]:
                return [0]
            else:
                return [-1]
        start_to_idx = dict()
        start_list = []
        for idx,interval in enumerate(intervals):
            start_to_idx[interval[0]] = idx
            start_list.append(interval[0])
        start_list.sort()
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        curr = 0
        result = [-1] * n
        for interval in intervals:
            while curr < n and start_list[curr] < interval[1]:
                curr += 1
            if curr >= n:
                continue
            result[start_to_idx[interval[0]]] = start_to_idx[start_list[curr]]
        return result
