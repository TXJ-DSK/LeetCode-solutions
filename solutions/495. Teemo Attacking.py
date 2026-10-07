# O(N) time, O(1) space
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        start, end = timeSeries[0], timeSeries[0]
        result = 0
        for t in timeSeries:
            if t <= end:
                end = t + duration
            else:
                result += (end - start)
                start, end = t, t + duration
        return result + end - start
