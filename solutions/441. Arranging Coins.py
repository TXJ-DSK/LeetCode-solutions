# O(1) time, O(1) space
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # find max r: (r+1) * r / 2 <= n
        r = math.floor(math.sqrt(n * 2))
        while r * (r+1) <= n * 2:
            r += 1
        return r-1
