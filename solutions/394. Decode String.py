class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        result = ""
        stack_level = 0
        digit_stack = []
        stack = []
        for c in s:
            if c.isdigit():
                if len(digit_stack) <= stack_level:
                    digit_stack.append(c)
                else:
                    digit_stack[stack_level] = digit_stack[stack_level] + c
            elif c == '[':
                stack_level += 1
                stack.append("")
            elif c == ']':
                stack_level -= 1
                if stack_level == 0:
                    result = result + stack[0] * int(digit_stack[0])
                else:
                    stack[-2] = stack[-2] + stack[-1] * int(digit_stack[-1])
                stack.pop(-1)
                digit_stack.pop(-1)
            else:
                if stack_level == 0:
                    result = result + c
                else:
                    stack[stack_level-1] = stack[stack_level-1] + c
        return result
