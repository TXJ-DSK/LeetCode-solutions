# Using a doublylinkedlist and two dicts, O(n) time
class DoublyListNode:
    key = 0
    prevNode = None
    nextNode = None
    def __init__(self, key, prevNode=None, nextNode=None):
        self.key = key
        self.prevNode = prevNode
        self.nextNode = nextNode

class LRUCache:

    def __init__(self, capacity: int):
        self.existKeys = dict()
        self.keyNodes = dict()
        self.capacity = capacity
        self.head = DoublyListNode(-1)
        self.tail = DoublyListNode(99999,self.head)
        self.head.nextNode = self.tail

    def removeNode(self, key):
        node = self.keyNodes[key]
        prev_node = node.prevNode
        next_node = node.nextNode
        prev_node.nextNode = next_node
        next_node.prevNode = prev_node
    
    def reposition(self, key):
        self.removeNode(key)
        node = self.keyNodes[key]
        prev_head = self.head.nextNode
        self.head.nextNode, node.nextNode = node, prev_head
        node.prevNode, prev_head.prevNode = self.head, node
    
    def insertHead(self, node):
        prev_head = self.head.nextNode
        self.head.nextNode, node.nextNode = node, prev_head
        node.prevNode, prev_head.prevNode = self.head, node

    def printLL(self):
        node = self.head
        while node is not None:
            print(node.key, "->", end='')
            node = node.nextNode
        print("")

    def get(self, key: int) -> int:
        if key in self.existKeys.keys():
            self.reposition(key)
            return self.existKeys[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.existKeys.keys():
            self.reposition(key)
            self.existKeys[key] = value
            return
        node = DoublyListNode(key)
        self.keyNodes[key] = node
        if len(self.existKeys) < self.capacity:
            self.existKeys[key] = value
            self.insertHead(node)
        else:
            lru = self.tail.prevNode.key
            del self.existKeys[lru]
            self.removeNode(lru)
            del self.keyNodes[lru]
            self.existKeys[key] = value
            self.insertHead(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
