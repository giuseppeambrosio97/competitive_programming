class ProductOfNumbers:

    def __init__(self):
        self.v = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.v = [1]
            return
        self.v.append(num*self.v[-1])
        
    def getProduct(self, k: int) -> int:
        if len(self.v) <= k:
            return 0
        else:
            return self.v[-1] // self.v[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)