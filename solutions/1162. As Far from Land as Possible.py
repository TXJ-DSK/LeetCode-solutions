# BFS
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        currDist = []
        nextDist = []
        distance = 0
        isWater = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    isWater = True
                else:
                    currDist.append((i, j))
        if len(currDist) == 0:
            return -1
        if not isWater:
            return -1
        def checkWater(i, j, distance) -> bool:
            if i>=0 and j>=0 and i<n and j<n and grid[i][j] == 0:
                grid[i][j] = distance + 1
                return True
            return False
        while len(currDist) > 0:
            distance = grid[currDist[0][0]][currDist[0][1]]
            for coor in currDist:
                i, j = coor[0], coor[1]
                if checkWater(i+1, j, distance):
                    nextDist.append((i+1, j))
                if checkWater(i-1, j, distance):
                    nextDist.append((i-1, j))
                if checkWater(i, j+1, distance):
                    nextDist.append((i, j+1))
                if checkWater(i, j-1, distance):
                    nextDist.append((i, j-1))
            currDist = nextDist
            nextDist = []
        return distance-1 # all land distance start with 1
