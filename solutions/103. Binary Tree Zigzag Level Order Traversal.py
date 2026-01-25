# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr_lvl = [root]
        result = []
        isForward = True
        while len(curr_lvl) > 0:
            next_lvl = []
            values = []
            for node in curr_lvl:
                values.append(node.val)
                if node.left is not None:
                    next_lvl.append(node.left)
                if node.right is not None:
                    next_lvl.append(node.right)
            if isForward:
                result.append(values)
            else:
                result.append(values[::-1])
            isForward = not isForward
            curr_lvl = next_lvl
        return result
