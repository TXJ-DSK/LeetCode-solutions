# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if k == 0:
            return head
        n = 1
        tail = head
        while tail.next is not None:
            n += 1
            tail = tail.next
        k = k % n
        if k == 0:
            return head
        displacement = n - k - 1
        new_tail = head
        for _ in range(displacement):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        return new_head
        
