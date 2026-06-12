# O(N) Time, O(1) Space
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        d1 = 0
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                d1 = i - 0
                break
        d2 = 0
        for i in range(n):
            if colors[i] != colors[n-1]:
                d2 = n-1 - i
                break
        return max(d1, d2)
