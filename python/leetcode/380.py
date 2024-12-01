import random


class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        self.h[val] = len(self.h)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        
        idval = self.h[val]
        lastval = self.nums[-1]
        self.h[lastval] = idval
        self.nums[idval] = lastval
        del self.h[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        n = len(self.nums)
        randid = random.randint(0,n-1)
        return self.nums[randid]