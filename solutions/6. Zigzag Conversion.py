class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [""] * numRows
        currRow = 0
        isDown = True
        for c in s:
            result[currRow] += c
            if isDown:
                if currRow < numRows - 1:
                    currRow += 1
                else:
                    currRow -= 1
                    isDown = not isDown
            else:
                if currRow > 0:
                    currRow -= 1
                else:
                    currRow += 1
                    isDown = not isDown
        return "".join(result)
