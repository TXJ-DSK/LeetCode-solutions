# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # handle n = 0
            return head
        odd_head = None
        odd_tail = None
        even_head = None
        even_tail = None
        curr = head
        count = 1
        while curr is not None:
            if count % 2 == 0:
                #even
                if even_head is None:
                    even_head = curr
                    even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr
            else:
                #odd
                if odd_head is None:
                    odd_head = curr
                    odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr
            curr = curr.next
            count += 1
        # add evens to the end of odds
        odd_tail.next = even_head
        if even_tail: # avoid access even_tail.next when even_tail is None
            even_tail.next = None # clean residual last odd node
        return odd_head
