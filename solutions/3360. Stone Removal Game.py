# O(N) time, O(1) space
class Solution:
    def canAliceWin(self, n: int) -> bool:
        result = False
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1
            result = not result
        return result
