# O(logN) Time, O(logN) Space
class Solution:
    def reverse(self, x: int) -> int:
        upperbound = pow(2, 31) - 1
        lowerbound = pow(-2, 31)
        if x == 0:
            return 0
        isNeg = x < 0
        int_str = str(x)
        if isNeg:
            int_str = int_str[1:]
        result_str = int_str[::-1]
        multiplier = 1
        if isNeg:
            multiplier = -1
        if int(result_str) * multiplier < lowerbound or int(result_str) * multiplier > upperbound:
            return 0
        else:
            return int(result_str) * multiplier
