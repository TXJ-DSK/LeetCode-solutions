# O(N) time, O(1) space, N is the length of columnTitle
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        result = 0
        for char in columnTitle[::-1]:
            result += (ord(char) - ord('A') + 1) * base
            base *= 26
        return result
