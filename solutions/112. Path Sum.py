# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.recursive(root, targetSum, 0)
        
    def recursive(self, node: Optional[TreeNode], targetSum: int, prev: int) -> bool:
        if node is None:
            return False
        if node.left is None and node.right is None:
            return node.val + prev == targetSum
        else:
            return self.recursive(node.left, targetSum, prev+node.val) or self.recursive(node.right, targetSum, prev+node.val)
        
