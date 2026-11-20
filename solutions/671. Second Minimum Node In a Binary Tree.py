# O(N) time, O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        arr = [root.val, sys.maxsize]
        def dfs(node, arr):
            if not node:
                return
            if node.val > arr[0] and node.val < arr[1]:
                arr[1] = node.val
            dfs(node.left, arr)
            dfs(node.right, arr)
        dfs(root, arr)
        if arr[1] == sys.maxsize:
            return -1
        else:
            return arr[1]
