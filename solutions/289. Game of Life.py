# Use numbers to temporarily store the previous state of cell
# 2: was 0 will change to 1
# 3: was 1 will change to 0
# 1 & 0 will not change
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def tempUpdate(i, j):
            neighbors = 0
            for row in (i-1, i, i+1):
                for col in (j-1, j, j+1):
                    if row>=0 and col>=0 and row<m and col<n:
                        neighbors += board[row][col] % 2
            neighbors -= board[i][j] % 2 #Exclude itself
            if board[i][j] % 2 == 0:
                if neighbors == 3:
                    board[i][j] = 2
            else:
                if neighbors < 2:
                    board[i][j] = 3
                elif neighbors > 3:
                    board[i][j] = 3
        
        for i in range(m):
            for j in range(n):
                tempUpdate(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
