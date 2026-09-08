# O(1) time, O(1) space
class Solution:
    def countCommas(self, n: int) -> int:
        # since n <= 10^5
        return max(0, n-999)
