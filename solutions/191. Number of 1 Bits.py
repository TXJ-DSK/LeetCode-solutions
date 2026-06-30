# O(logN) Time, O(1) Space
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            result += n % 2
            n = n // 2
        return result
