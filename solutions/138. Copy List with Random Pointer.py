"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:  # handle n = 0
            return None
        if head.next is None:  # handle n = 1
            new_head = Node(head.val)
            if head.random:
                new_head.random = new_head
            return new_head
        old_curr = head
        new_head = Node(head.val, None, head.random)
        new_curr = new_head
        # Create deep copy
        while old_curr.next is not None:
            # Assign the random pointer of old node to its corresponding new node(of the same index)
            old_curr.random = new_curr
            old_curr = old_curr.next
            new_node = Node(old_curr.val, None, old_curr.random)
            new_curr.next = new_node
            new_curr = new_node
        old_curr.random = new_curr
        # In the second iteration, update the random pointer to new nodes in new linked list
        node_iter = new_head
        while node_iter is not None:
            old_node = node_iter.random
            if old_node:
                node_iter.random = old_node.random
            node_iter = node_iter.next
        return new_head
