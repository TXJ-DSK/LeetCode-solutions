# DFS with visited memory, O(M*N) Time, O(M*N) Space
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        m, n = len(board), len(board[0])
        for i in range(n):
            if board[0][i] == "O":
                visited.add((0,i))
            if board[m-1][i] == "O":
                visited.add((m-1,i))
        for j in range(m):
            if board[j][0] == "O":
                visited.add((j,0))
            if board[j][n-1] == "O":
                visited.add((j,n-1))
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if (i,j) in visited:
                return
            if board[i][j] == "X":
                return
            visited.add((i,j))
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        border = list(visited)
        for i, j in border:
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"

        
