# O(logN) time, O(1) space
class Solution:
    def maxProduct(self, n: int) -> int:
        max1, max2 = 0, 0
        while n > 0:
            d = n % 10
            if d > max2:
                max2 = d
                max1, max2 = max(max1, max2), min(max1, max2)
            n = n // 10
        return max1 * max2
