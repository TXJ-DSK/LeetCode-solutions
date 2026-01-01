class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        allHappy = 3
        for i in range(1,n):
            allHappy *= 2
        if k > allHappy:
            return ""
        if n == 1:
            return chr(ord('a')+k-1)
        result = 'a'
        #print(f"allHappy={allHappy}")
        allHappy = allHappy // 3
        while k > allHappy:
            result = chr(ord(result[0]) + 1)
            k -= allHappy
        letters = ['a', 'b', 'c']
        while len(result) < n:
            available = [c for c in letters if c != result[-1]]
            allHappy = allHappy // 2
            if k > allHappy:
                result = result + available[1]
                k -= allHappy
            else:
                result = result + available[0]
        return result
