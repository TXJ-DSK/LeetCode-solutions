# O(N) Time, O(1) Space
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            weight_sum = 0
            for c in word:
                weight_sum += weights[ord(c)-ord('a')]
            result += chr(ord('z') - (weight_sum % 26))
        return result
