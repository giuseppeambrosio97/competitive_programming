import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        def is_good(t: int) -> bool:
            c, i = cars, 0
            while i < n and c > 0:
                ## how many cars can be repaired with rank r in time t?
                ## largest n such that r*n^2 <= t
                ## n <= sqrt(t//r) -> 
                c -= math.floor(math.sqrt(t//ranks[i]))
                i += 1
            return c <= 0

        l, r = 1, min(ranks)*cars**2
        res = math.inf
        while l <= r:
            m = l + (r-l)//2

            if is_good(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res