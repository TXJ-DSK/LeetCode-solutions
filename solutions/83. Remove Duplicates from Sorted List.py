# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr is None: # handle n = 0
            return head
        while curr.next is not None:
            next_n = curr.next
            if curr.val == next_n.val:
                # skip the next node if it is a duplicate
                curr.next = next_n.next
            else:
                curr = next_n
        return head
