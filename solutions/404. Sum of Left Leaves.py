# O(N) time, O(1) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)
            return dfs(node.left) + dfs(node.right)
        return dfs(root)
