# O(NlogN) time, O(1) extra space
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i, j = 0, 0
        n, m = len(g), len(s)
        result = 0
        while i<n and j<m:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                i += 1
        return result
