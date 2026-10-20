# O(N) time, O(N) space
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        n = len(s)
        for start in range(0, n, 2*k):
            for i in range(start+k-1,start-1,-1):
                if i >= n:
                    continue
                result += s[i]
            for i in range(start+k,start+2*k):
                if i >= n:
                    continue
                result += s[i]
        return result
