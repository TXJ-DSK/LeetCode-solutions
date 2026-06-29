class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for s in patterns:
            if s in word:
                result += 1
        return result
