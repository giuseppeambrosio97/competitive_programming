from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_good(k: int) -> bool:
            s = [math.ceil(p/k) for p in piles]
            return sum(s) <= h

        n = len(piles)
        max_ = max(piles)
        if n == h:
            return max_
        
        l, r = 1, max_

        while l <= r:
            m = (r + l) // 2

            if m == 1 and is_good(1):
                return 1
            
            if is_good(m):
                if not is_good(m-1):
                    return m
                r = m - 1
            else:
                l = m + 1

        return l


if __name__ == '__main__':
    piles = [3,6,7,11]
    h = 18
    s = Solution().minEatingSpeed(piles, h)

    print(s)