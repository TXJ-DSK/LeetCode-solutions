# O(N) Time, O(1) Space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        fast, slow = dummy_head, dummy_head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
