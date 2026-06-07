# O(N) Time, O(1) Space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        left_dict, right_dict = dict(), dict()
        children_set = set()
        for des in descriptions:
            if des[2] == 1:
                left_dict[des[0]] = des[1]
            else:
                right_dict[des[0]] = des[1]
            children_set.add(des[1])
        root_val = None
        for parent in left_dict:
            if parent not in children_set:
                root_val = parent
        for parent in right_dict:
            if parent not in children_set:
                root_val = parent
        if root_val is None:
            raise Exception("Invalid tree")
        '''
        print("root_val=",root_val)
        print("left_dict=",left_dict)
        print("right_dict=",right_dict)
        '''
        root = TreeNode(root_val)

        def buildTree(node):
            if node is None:
                return
            if node.val in left_dict:
                node.left = TreeNode(left_dict[node.val])
                buildTree(node.left)
            if node.val in right_dict:
                node.right = TreeNode(right_dict[node.val])
                buildTree(node.right)
        
        buildTree(root)
        return root
