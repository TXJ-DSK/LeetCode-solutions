# O(N) time, O(N) space
from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        occurences = Counter()
        def dfs(node):
            if not node:
                return
            occurences[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_occ, max_vals = 0, []
        for val in occurences.keys():
            if occurences[val] > max_occ:
                max_occ = occurences[val]
                max_vals = [val]
            elif occurences[val] == max_occ:
                max_vals.append(val)
        return max_vals
