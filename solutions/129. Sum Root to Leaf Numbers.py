# Recursive DFS, O(N) time, O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursive(node, val):
            newval = val * 10 + node.val
            if not node.left and not node.right:
                return newval
            result = 0
            if node.left:
                result += recursive(node.left, newval)
            if node.right:
                result += recursive(node.right, newval)
            return result
        
        return recursive(root, 0)
