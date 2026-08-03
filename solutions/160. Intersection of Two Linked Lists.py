# O(M+N) time, O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        lenA, lenB = 0, 0
        curr = headA
        while curr is not None:
            lenA += 1
            curr = curr.next
        curr = headB
        while curr is not None:
            lenB += 1
            curr = curr.next
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        while headA is not None and headB is not None:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            
