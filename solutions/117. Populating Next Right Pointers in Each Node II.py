# DFS, O(N) time, O(1) space
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root: 'Optional[Node]', myright: 'Optional[Node]'):
            if root is None:
                return
            root.next = myright
            childright = None
            while myright is not None:
                if myright.left is not None:
                    childright = myright.left
                    break
                elif myright.right is not None:
                    childright = myright.right
                    break
                myright = myright.next
            if root.left and root.right:
                dfs(root.right, childright)
                dfs(root.left, root.right)
            elif root.left and not root.right:
                dfs(root.left, childright)
            elif not root.left and root.right:
                dfs(root.right, childright)
        dfs(root, None)
        return root
