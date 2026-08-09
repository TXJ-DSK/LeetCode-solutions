# space optimized, O(N) time, O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        #print(f"slow={slow.val}")
        # reverse second part
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        tail = prev
        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True
