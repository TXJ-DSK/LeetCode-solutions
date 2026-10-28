# O(N) time, O(N) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0
            leftTilt, leftSum, leftTiltSum = dfs(node.left)
            rightTilt, rightSum, rightTiltSum = dfs(node.right)
            return abs(leftSum - rightSum), leftSum + rightSum + node.val, leftTiltSum + rightTiltSum + abs(leftSum - rightSum)
        rootTilt, rootSum, rootTiltSum = dfs(root)
        return rootTiltSum
