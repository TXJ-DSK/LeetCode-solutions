# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy_head = ListNode(10000)
        tail = dummy_head
        k = len(lists)
        vals = [10000] * k
        for i in range(k):
            if lists[i] is None:
                continue
            vals[i] = lists[i].val
            lists[i] = lists[i].next
        while min(vals) < 10000:
            min_val = min(vals)
            idx = vals.index(min_val)
            tail.next = ListNode(min_val)
            tail = tail.next
            if lists[idx] is None:
                vals[idx] = 10000
            else:
                vals[idx] = lists[idx].val
                lists[idx] = lists[idx].next
        return dummy_head.next
