# BFS iterative approach, O(n) time and space complexity

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        curr_level = [root]
        while len(curr_level) > 0:
            total = 0
            next_level = []
            for node in curr_level:
                total += node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            result.append(total / len(curr_level))
            curr_level = next_level
        return result
