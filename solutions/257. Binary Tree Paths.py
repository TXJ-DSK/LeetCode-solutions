# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        currLevel = [[root, []]]
        nextLevel = []
        while len(currLevel) > 0:
            for item in currLevel:
                node = item[0]
                pathValues = item[1].copy()
                pathValues.append(str(node.val))
                if node.left is None and node.right is None:
                    results.append("->".join(pathValues))
                if node.left:
                    nextLevel.append([node.left,pathValues])
                if node.right:
                    nextLevel.append([node.right,pathValues])
            currLevel = nextLevel
            nextLevel = []
        return results
