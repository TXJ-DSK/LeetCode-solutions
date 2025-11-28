# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-9999, None)
        curr = head
        while curr:
            original_next = curr.next
            sorted_curr = dummy_head
            sorted_next = sorted_curr.next
            while sorted_next:
                if sorted_next.val > curr.val:
                    sorted_curr.next = curr
                    curr.next = sorted_next
                    break
                else:
                    sorted_curr = sorted_next
                    sorted_next = sorted_curr.next
            if not sorted_next:
                sorted_curr.next = curr
                curr.next = None
            curr = original_next
        return dummy_head.next
