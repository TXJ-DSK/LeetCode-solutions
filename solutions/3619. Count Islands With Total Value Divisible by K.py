# O(M*N) time, O(1) extra space
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x: int,y: int) -> int:
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0
            if grid[x][y] == 0:
                return 0
            total = grid[x][y]
            grid[x][y] = 0
            return total + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y+1) + dfs(x, y-1)
        result = 0
        for i in range(m):
            for j in range(n):
                value = dfs(i, j)
                if value > 0 and value % k == 0:
                    result += 1
        return result
