# O(N) time, O(1) space
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = [0] * 26
        n = len(s)
        head, tail = 0, 0
        result = 0
        while tail < n:
            idx = ord(s[tail])-ord('a')
            cnt[idx] += 1
            while cnt[idx] > 2:
                cnt[ord(s[head])-ord('a')] -= 1
                head += 1
            tail += 1
            result = max(result, tail - head)
        return result
