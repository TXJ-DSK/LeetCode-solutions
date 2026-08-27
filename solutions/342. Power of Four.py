# O(logN) time, O(logN) space
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        b_str = bin(n)[2:]
        return n > 0 and len(b_str) % 2 == 1 and b_str.count('1') == 1
