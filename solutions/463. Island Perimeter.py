# O(M*N) time, O(1) space
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def inRange(x, y):
            return 0 <= x < row and 0 <= y < col
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result += 4
                    for x in (i+1, i-1):
                        if inRange(x,j) and grid[x][j] == 1:
                            result -= 1
                    for y in (j+1, j-1):
                        if inRange(i,y) and grid[i][y] == 1:
                            result -= 1
        return result
