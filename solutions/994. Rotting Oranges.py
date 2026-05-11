# BFS, O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        currRot = []
        nextRot = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    pos = (i, j)
                    currRot.append(pos)
        def infect(i, j) -> bool:
            if i>=0 and i<m and j>=0 and j<n and grid[i][j] == 1:
                grid[i][j] = 2
                return True
            return False
        while len(currRot) > 0:
            for pos in currRot:
                i, j = pos[0], pos[1]
                if infect(i+1, j):
                    nextRot.append((i+1, j))
                if infect(i-1, j):
                    nextRot.append((i-1, j))
                if infect(i, j+1):
                    nextRot.append((i, j+1))
                if infect(i, j-1):
                    nextRot.append((i, j-1))
            if len(nextRot) > 0:
                result += 1
            currRot = nextRot
            nextRot = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return result
