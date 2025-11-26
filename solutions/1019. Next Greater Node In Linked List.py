# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [0]
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        result = [0] * len(nums)
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(nums[i])
        
        return result
        
