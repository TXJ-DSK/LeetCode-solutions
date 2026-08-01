# DP method, O(N^2) time, O(N) space
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        while len(row) < rowIndex+1:
            newrow = [1]
            for i in range(len(row)-1):
                newrow.append(row[i] + row[i+1])
            newrow.append(1)
            row = newrow
        return row
