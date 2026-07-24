# DFS approach, O(N) time, O(1) space, BFS would take O(N) space in worst case
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 99999
            if not node.left and not node.right:
                return 1
            return min(dfs(node.left), dfs(node.right)) + 1
        if not root:
            return 0
        return dfs(root)
