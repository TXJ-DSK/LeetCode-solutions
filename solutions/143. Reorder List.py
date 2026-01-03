# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        while curr is not None and curr.next is not None and curr.next.next is not None:
            tail_prev = curr
            while tail_prev.next.next is not None:
                tail_prev = tail_prev.next
            curr_next = curr.next
            curr.next = tail_prev.next
            tail_prev.next.next = curr_next
            tail_prev.next = None
            curr = curr_next
