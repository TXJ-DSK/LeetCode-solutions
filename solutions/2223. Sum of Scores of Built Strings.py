class Solution:
    def sumScores(self, s: str) -> int:
        total_score = 0
        for i in range(len(s)):
            result = self.binarySearch(i,s)
            if result > 0:
                score = result - i + 1
                total_score += score
        return total_score
    
    def binarySearch(self, start: int, s: str) -> int:
        left = start
        right = len(s)-1
        result = -1
        while right >= left:
            mid = left + (right - left) // 2
            prefix = s[start:mid+1]
            if prefix == s[:len(prefix)]:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
