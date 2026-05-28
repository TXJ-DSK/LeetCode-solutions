# DFS recursive, O(N) time, O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        def recursive(node: Optional[TreeNode]):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            if not node.left and node.right:
                return recursive(node.right)
            if node.left and not node.right:
                node.right = node.left
                node.left = None
                return recursive(node.right)
            oldright = node.right
            node.right = node.left
            node.left = None
            tail = recursive(node.right)
            tail.right = oldright
            return recursive(oldright)

        recursive(root)
        
