# O(N) space, O(1) time for both function call
class ProductOfNumbers:

    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
        else:
            if len(self.products) > 0:
                self.products.append(self.products[-1]*num)
            else:
                self.products.append(num)
        

    def getProduct(self, k: int) -> int:
        if k > len(self.products):
            return 0
        elif k == len(self.products):
            return self.products[-1]
        return self.products[-1] // self.products[0-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
