# O(M * N) Time, O(M * N) Space
from collections import deque
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        #safety = [[-1 for _ in range(n)] for _ in range(m)]
        safety = dict()
        d = deque()
        d.append((0, 0, health))
        while len(d) > 0:
            i, j, h = d.popleft()
            #if safety[i][j] >= h:
            if (i, j) in safety and safety[(i, j)] >= h:
                continue
            if h == 0:
                continue
            penalty = grid[i][j]
            safety[(i, j)] = h-penalty
            if i > 0:
                d.append((i-1, j, h-penalty))
            if i < m-1:
                d.append((i+1, j, h-penalty))
            if j > 0:
                d.append((i, j-1, h-penalty))
            if j < n-1:
                d.append((i, j+1, h-penalty))
        if (m-1, n-1) not in safety:
            return False
        return safety[(m-1, n-1)] > 0
            
            
