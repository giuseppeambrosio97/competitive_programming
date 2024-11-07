from collections import deque


class StockSpanner:

    def __init__(self):
        self.i = 0
        self.s = deque()

    def next(self, price: int) -> int:
        while len(self.s) != 0 and self.s[-1][0] <= price:
            self.s.pop()

        self.i += 1
        if len(self.s) == 0:
            self.s.append((price,self.i))
            return self.i

        span = self.i - self.s[-1][1]
        self.s.append((price,self.i))    
        return span 


if __name__ == '__main__':
    stockSpanner = StockSpanner()
    print(stockSpanner.next(1), end=" ")
    print(stockSpanner.next(79), end=" ")
    print(stockSpanner.next(34), end=" ")
    print(stockSpanner.next(21), end=" ")
    print(stockSpanner.next(34), end=" ")
    print(stockSpanner.next(16), end=" ")
    print(stockSpanner.next(59), end=" ")
    print(stockSpanner.next(63), end=" ")
    print(stockSpanner.next(72), end=" ")
    print(stockSpanner.next(5))