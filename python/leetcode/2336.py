import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.q = list(range(1,1001))
        heapq.heapify(self.q)
        self.available = set(range(1,1001))

    def popSmallest(self) -> int:
        """T(n) = O(logn)"""
        el = heapq.heappop(self.q)
        self.available.remove(el)
        return el

    def addBack(self, num: int) -> None:
        """T(n) = O(logn)"""
        if num not in self.available:
            self.available.add(num)
            heapq.heappush(self.q, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
if __name__ == '__main__':
    h = SmallestInfiniteSet()

    h.addBack(2)
    print(h.popSmallest())
    h.addBack(4)
    print(h.q)

    