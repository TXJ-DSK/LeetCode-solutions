# O(N) time, O(N) space
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nexts = ""
            chunks = [s[i:i + k] for i in range(0, len(s), k)]
            for chunk in chunks:
                digitSum = 0
                for d in chunk:
                    digitSum += int(d)
                nexts += str(digitSum)
            s = nexts
        return s
