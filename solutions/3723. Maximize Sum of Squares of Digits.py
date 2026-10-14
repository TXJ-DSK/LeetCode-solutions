# O(1) time, O(1) extra space
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        result = ""
        if sum > num * 9:
            return ""
        if sum >= 9:
            digits = min(sum//9, num)
            result = result + "9" * digits
            sum -= 9 * digits
        if len(result) < num:
            result = result + str(sum)
            sum -= sum
        if len(result) < num:
            result = result + "0" * (num - len(result))
        return result
