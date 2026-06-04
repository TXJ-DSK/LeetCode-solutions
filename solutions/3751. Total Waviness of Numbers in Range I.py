# O(N) brute force

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        for num in range(num1, num2+1):
            if num<100:
                continue
            s = str(num)
            for i in range(1,len(s)-1):
                if s[i-1] < s[i] and s[i+1] < s[i]:
                    result += 1
                elif s[i-1] > s[i] and s[i+1] > s[i]:
                    result += 1
        return result
