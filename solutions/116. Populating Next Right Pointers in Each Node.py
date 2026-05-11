# DFS O(n) time O(1) space
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
        def dfs(root: 'Optional[Node]', myRight: 'Optional[Node]'):
            if root is None:
                return
            root.next = myRight
            if root.left is None:
                return
            if myRight is not None:
                dfs(root.right, myRight.left)
            else:
                dfs(root.right, None)
            dfs(root.left, root.right)
        dfs(root, None)
        return root
