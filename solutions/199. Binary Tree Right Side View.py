# BFS iterative, O(n) time and space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        curr_level = [root]
        while len(curr_level) > 0:
            result.append(curr_level[-1].val)
            next_level = []
            for node in curr_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            curr_level = next_level
        return result
