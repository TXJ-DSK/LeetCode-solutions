# O(N) time, O(1) extra space
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = ""
        for i in range(len(s)):
            if s[i] == ' ':
                result = result + word + ' '
                word = ""
            else:
                word = s[i] + word
        return result + word
