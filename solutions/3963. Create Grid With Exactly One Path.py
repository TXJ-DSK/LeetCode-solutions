# O(M+N) time, O(M+N) space
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = ['.' * n]
        row = '#'*(n-1)+'.'
        return result + [row] * (m-1)
