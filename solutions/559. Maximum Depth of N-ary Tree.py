# O(N) time, O(N) space
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            if len(node.children) == 0:
                return 1
            return max([dfs(child) for child in node.children])+1
        return dfs(root)
