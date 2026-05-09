# O(nlogn) for balanced tree, O(n^2) for single sided tree
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        result = 0
        currLevel = [[root, []]]
        nextLevel = []
        while len(currLevel) > 0:
            for item in currLevel:
                node = item[0]
                pathSums = item[1].copy()
                for i in range(len(pathSums)):
                    pathSums[i] += node.val
                pathSums.append(node.val)
                result += pathSums.count(targetSum)
                if node.left:
                    nextLevel.append([node.left, pathSums])
                if node.right:
                    nextLevel.append([node.right, pathSums])
            
            currLevel = nextLevel
            nextLevel = []
        return result
