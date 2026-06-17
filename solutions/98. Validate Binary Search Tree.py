# DFS, O(N) Time, O(1) Space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, upperbound, lowerbound):
            if not node:
                return True
            if node.val >= upperbound or node.val <= lowerbound:
                return False
            left_valid = dfs(node.left, min(node.val, upperbound), lowerbound)
            right_valid = dfs(node.right, upperbound, max(lowerbound, node.val))
            return left_valid and right_valid
        
        return dfs(root, int(sys.maxsize), -1 * int(sys.maxsize))
