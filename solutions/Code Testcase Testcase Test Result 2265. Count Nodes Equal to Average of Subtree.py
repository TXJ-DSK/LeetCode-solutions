# O(N) time, O(1) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            # subtree sum, subnode count, number of average nodes
            result = [node.val, 1, 0]
            if node.left:
                left_result = dfs(node.left)
                for i in range(3):
                    result[i] += left_result[i]
            if node.right:
                right_result = dfs(node.right)
                for i in range(3):
                    result[i] += right_result[i]
            if node.val == result[0] // result[1]:
                #print("avg node=",node.val)
                result[2] += 1
            return result
        return dfs(root)[2]
