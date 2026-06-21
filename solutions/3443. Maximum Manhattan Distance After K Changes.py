# O(N) Time, O(1) Space
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        result = 0
        n0,s0,e0,w0 = 0,0,0,0
        for c in s:
            match c:
                case 'N':
                    n0 += 1
                case 'S':
                    s0 += 1
                case 'E':
                    e0 += 1
                case 'W':
                    w0 += 1
            dist = abs(n0-s0) + abs(e0-w0)
            max_potential = min(n0, s0) + min(e0, w0)
            result = max(result, dist + 2 * min(k, max_potential))
        return result
