class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isFirstRow = False
        isFirstCol = False
        m, n = len(matrix), len(matrix[0])
        #print(f"m={m},n={n}")
        for i in matrix[0]:
            if i == 0:
                isFirstRow = True
                break
        for row in matrix:
            if row[0] == 0:
                isFirstCol = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        #print(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    #print(f"i={i},j={j}")
                    matrix[i][j] = 0
        if isFirstRow:
            for i in range(n):
                matrix[0][i] = 0
        if isFirstCol:
            for i in range(m):
                matrix[i][0] = 0
