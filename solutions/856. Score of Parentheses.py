# O(N) time, O(N) space
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                A = 0
                while stack[-1] != '(':
                    A += stack.pop(-1)
                stack.pop(-1)
                if A > 0:
                    stack.append(2 * A)
                else:
                    stack.append(1)
        return sum(stack)
