# BFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        currLevel = [root]
        nextLevel = []
        while len(currLevel) > 0:
            levelValues = []
            for node in currLevel:
                levelValues.append(node.val)
                for child in node.children:
                    if child is not None:
                        nextLevel.append(child)
            result.append(levelValues)
            currLevel = nextLevel
            nextLevel = []
        return result
