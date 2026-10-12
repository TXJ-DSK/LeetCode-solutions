# O(logN) time, O(logN) space
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        isNeg = False
        if num < 0:
            isNeg = True
            num = -1 * num
        result = ""
        while num > 0:
            result += str(num % 7)
            num = num // 7
        if isNeg:
            return '-' + result[::-1]
        else:
            return result[::-1]
