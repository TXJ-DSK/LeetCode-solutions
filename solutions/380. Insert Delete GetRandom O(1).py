class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.int_idx = dict()

    def insert(self, val: int) -> bool:
        if val not in self.int_idx:
            self.int_idx[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.int_idx:
            last = self.arr.pop()
            if last == val:
                del self.int_idx[val]
                return True
            else:
                pos = self.int_idx[val]
                self.int_idx[last] = pos
                self.arr[pos] = last
                del self.int_idx[val]
                return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
