# O(N) time, O(1) space
class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        consecutive_L = 0
        for c in s:
            if c == 'A':
                A_count += 1
                if A_count == 2:
                    return False
            if c == 'L':
                consecutive_L += 1
                if consecutive_L == 3:
                    return False
            else:
                consecutive_L = 0
        return True
