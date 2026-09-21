class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry, d1, d2 = 0, 0, 0
        result = ""
        n = max(len(num1), len(num2))
        for i in range(n):
            i1 = len(num1) - 1 - i
            i2 = len(num2) - 1 - i
            if i1 > -1:
                d1 = int(num1[i1])
            if i2 > -1:
                d2 = int(num2[i2])
            dsum = d1 + d2 + carry
            carry = 0
            if dsum > 9:
                carry = 1
                dsum -= 10
            result = str(dsum) + result
            d1, d2 = 0, 0
        if carry > 0:
            result = str(carry) + result
        return result
