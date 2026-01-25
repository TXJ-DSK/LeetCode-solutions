# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-999)
        prev = -999
        curr = dummy
        while head is not None:
            if head.val == prev:
                head = head.next
                continue
            if head.next is None or head.val != head.next.val:
                prev = head.val
                curr.next = head
                curr = curr.next
                head_next = head.next
                head.next = None
                head = head_next
                continue
            prev = head.val
            head = head.next
        return dummy.next
