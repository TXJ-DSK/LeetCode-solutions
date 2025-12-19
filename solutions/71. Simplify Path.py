class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
        for name in dirs:
            match name:
                case '':
                    continue
                case '.':
                    continue
                case '..':
                    if len(stack) > 0:
                        stack.pop(-1)
                case _:
                    stack.append(name)
        return '/' + '/'.join(stack)
