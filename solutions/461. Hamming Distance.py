# O(logN) time, O(1) space
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                result += 1
            x = x // 2
            y = y // 2
        return result
