# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        if left == right:
            return head
        dummy_head = ListNode(0,head)
        left_prev = dummy_head
        for _ in range(left - 1):
            left_prev = left_prev.next
        prev = left_prev
        curr = left_prev.next
        rev_end = curr
        for _ in range(right - left + 1):
            t = curr.next
            curr.next = prev
            prev, curr = curr, t
        left_prev.next = prev
        rev_end.next = curr
        return dummy_head.next
