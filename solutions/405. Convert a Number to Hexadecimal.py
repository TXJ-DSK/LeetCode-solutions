# O(logN) time, O(logN) space
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        if num > 0:
            s = ""
            while num > 0:
                remainder = num % 16
                if remainder > 9:
                    s += chr(ord('a')+remainder-10)
                else:
                    s += str(remainder)
                num = num // 16
            return s[::-1]
        else:
            n = abs(num)-1
            s = ""
            while n > 0:
                remainder = n % 16
                val = 15 - remainder
                if val > 9:
                    s += chr(ord('a')+val-10)
                else:
                    s += str(val)
                n = n // 16
            while len(s) < 8:
                s += 'f'
            return s[::-1]
