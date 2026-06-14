# O(N) Time, O(1) Space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast is not None:
            fast = fast.next.next
            slow = slow.next
        reverse_half = ListNode(-1, None)
        while slow is not None:
            temp = slow.next
            slow.next = reverse_half.next
            reverse_half.next = slow
            slow = temp
        reverse_half = reverse_half.next
        max_sum = -1
        while reverse_half is not None:
            max_sum = max(max_sum, reverse_half.val + head.val)
            reverse_half = reverse_half.next
            head = head.next
        return max_sum
