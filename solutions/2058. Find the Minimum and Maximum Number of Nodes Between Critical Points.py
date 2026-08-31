# O(N) time, O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [999999, -1]
        firstCP, prevCP = None, None
        cpIDX = 0
        while head.next and head.next.next:
            val0, val1, val2 = head.val, head.next.val, head.next.next.val
            cpIDX += 1
            head = head.next
            if (val1 < val0 and val1 < val2) or (val1 > val0 and val1 > val2):
                if firstCP is None:
                    firstCP = cpIDX
                    prevCP = cpIDX
                    continue
                result[0] = min(result[0], cpIDX - prevCP)
                result[1] = cpIDX - firstCP
                prevCP = cpIDX
        if result[0] == 999999:
            return [-1, -1]
        return result
