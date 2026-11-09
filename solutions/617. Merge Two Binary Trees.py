# DFS, O(N) time, O(N) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            if node1 and node2:
                return TreeNode(node1.val + node2.val, dfs(node1.left, node2.left), dfs(node1.right, node2.right))
            if node1 and not node2:
                return TreeNode(node1.val, dfs(node1.left, None), dfs(node1.right,None))
            if not node1 and node2:
                return TreeNode(node2.val, dfs(None, node2.left), dfs(None, node2.right))
            return None
        return dfs(root1, root2)
