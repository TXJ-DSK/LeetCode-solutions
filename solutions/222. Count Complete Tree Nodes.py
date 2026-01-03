# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        node = root
        left = 1
        while node.left is not None:
            left *= 2
            node = node.left
        right = left * 2 - 1
        result = left
        while left <= right:
            mid = left + (right - left) // 2
            curr = mid
            stack = [] # stack of operations (left or right) to reach mid node
            while curr > 1:
                stack.append(curr % 2)
                curr = curr // 2
            #print(f"mid={mid},stack={stack}")
            curr_node = root
            for remainder in reversed(stack):
                if remainder == 0:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            if curr_node is None:
                right = mid - 1
            else:
                left = mid + 1
                result = mid
        return result
