class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        prev = head
        end = head
        for _ in range(n):
            end = end.next
        if end is None:
            return head.next
        while end.next is not None:
            prev = prev.next
            end = end.next
        prev.next = prev.next.next
        return head
