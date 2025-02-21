from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.enc = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        encn = len(self.enc)
        if self.idx >= encn:
            return -1
        a = n
        while a > 0:
            t = self.enc[self.idx] - a
            if t >= 0:
                self.enc[self.idx] = t
                return self.enc[self.idx+1]
            a = -t
            self.idx += 2
            if self.idx >= encn:
                return -1
        
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)