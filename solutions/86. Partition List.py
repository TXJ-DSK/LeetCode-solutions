# O(N) time, O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        dummyhead1 = ListNode(-1)
        tail1 = dummyhead1
        dummyhead2 = ListNode(-1)
        tail2 = dummyhead2
        while head is not None:
            if head.val < x:
                tail1.next = head
                head = head.next
                tail1 = tail1.next
                tail1.next = None
            else:
                tail2.next = head
                head = head.next
                tail2 = tail2.next
                tail2.next = None

        if dummyhead1.next is None:
            return dummyhead2.next
        tail1.next = dummyhead2.next
        tail2.next = None
        return dummyhead1.next
