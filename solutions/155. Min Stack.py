class Node:
    def __init__(self, value, minValue):
        self.value = value
        self.minValue = minValue

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack)>0:
            prevMinValue = self.getMin()
            self.stack.append(Node(val,min(val,prevMinValue)))
        else:
            self.stack.append(Node(val,val))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1].value
        

    def getMin(self) -> int:
        return self.stack[-1].minValue
