# Union find solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [-1] * (m * n)
        
        def find(parent, pos, n):
            if parent[pos] == pos:
                return pos
            else:
                return find(parent, parent[pos], n)
        
        def unite(parent, pos1, pos2, n):
            rep1 = find(parent, pos1, n)
            rep2 = find(parent, pos2, n)
            parent[rep1] = rep2

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                pos = i * n + j
                parent[pos] = pos
                if j > 0 and grid[i][j-1] == "1":
                    unite(parent, pos-1, pos, n)
                if i > 0 and grid[i-1][j] == "1":
                    unite(parent, pos-n, pos, n)
        print(parent)
        uniques = set()
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                uniques.add(find(parent, pos, n))
        uniques.discard(-1)
        return len(uniques)

# DFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    result += 1
        return result

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j] != "1":
            return
        grid[i][j] = "-1" # visited
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
