# O(MN) time, O(MN) space
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        mn = m * n
        ans = [[-9999 for _ in range(n)] for _ in range(m)]
        for pos in range(mn):
            origin = (pos + mn - k) % mn
            ans[pos//n][pos%n] = grid[origin//n][origin%n]
        return ans
