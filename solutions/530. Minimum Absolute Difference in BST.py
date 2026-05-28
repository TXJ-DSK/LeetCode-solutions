# DFS recursive, O(N) time, O(1) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        
        def recursive(node):
            if not node.left and not node.right:
                return 100000, node.val, node.val
            min_diff = 100000
            tree_min, tree_max = None, None
            if node.left:
                left_min_diff, left_min, left_max = recursive(node.left)
                tree_min = left_min
                min_diff = min(min_diff, abs(node.val - left_max))
                min_diff = min(min_diff, left_min_diff)
            if node.right:
                right_min_diff, right_min, right_max = recursive(node.right)
                tree_max = right_max
                min_diff = min(min_diff, abs(node.val - right_min))
                min_diff = min(min_diff, right_min_diff)
            if tree_min is None:
                tree_min = node.val
            if tree_max is None:
                tree_max = node.val
            
            return min_diff, tree_min, tree_max
        
        result, _, _ = recursive(root)
        return result
        
