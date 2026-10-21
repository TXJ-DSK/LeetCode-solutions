# O(N) time, O(N) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # return depth, result
            if not node:
                return 0, 0
            left_depth, left_result = dfs(node.left)
            right_depth, right_result = dfs(node.right)
            return max(left_depth, right_depth)+1, max(left_depth+right_depth, left_result, right_result)
        depth, result = dfs(root)
        return result
            
