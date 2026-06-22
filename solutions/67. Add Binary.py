# O(N) Time, where N is the length of a and b
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        b1, b2, c = 0, 0, 0 # Binary bit 1, bit 2, and carry
        result = ""
        n = max(len(a),len(b))
        for i in range(n):
            if len(a) > i and a[i] == "1":
                b1 = 1
            else:
                b1 = 0
            if len(b) > i and b[i] == "1":
                b2 = 1
            else:
                b2 = 0
            bsum = b1 + b2 + c
            result += str(bsum % 2)
            c = bsum // 2
        if c == 1:
            result += "1"
        return result[::-1]
