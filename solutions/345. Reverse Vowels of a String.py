# O(N) time, O(N) space
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        chars = list(s)
        left, right = 0, len(chars)-1
        while left < right:
            if chars[left] not in vowels:
                left += 1
                continue
            if chars[right] not in vowels:
                right -= 1
                continue
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)
