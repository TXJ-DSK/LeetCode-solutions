# O(K) time, O(1) space, K is the length of ops
class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        x, y = m, n
        for op in ops:
            x = min(x, op[0])
            y = min(y, op[1])
        return x*y
