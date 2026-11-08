# O(M*N) time, O(1) extra space
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in range(m):
            server_count = 0
            for col in range(n):
                if grid[row][col] > 0:
                    server_count += 1
            if server_count > 1:
                for col in range(n):
                    if grid[row][col] > 0:
                        grid[row][col] = 2
        
        for col in range(n):
            server_count = 0
            for row in range(m):
                if grid[row][col] > 0:
                    server_count += 1
            if server_count > 1:
                for row in range(m):
                    if grid[row][col] > 0:
                        grid[row][col] = 2

        result = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    result += 1
        return result
