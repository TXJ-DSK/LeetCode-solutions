# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # handle n = 0
            return None
        if head.next is None: # handle n = 1
            return head
        curr = head
        new_head = ListNode(curr.val, None)
        while curr.next is not None:
            new_head = ListNode(curr.next.val, new_head)
            curr = curr.next
        return new_head

        
