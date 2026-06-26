# O(logN) Time, O(logN) Space
class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = f"{n:032b}"
        return int(binary_string[::-1], 2)
