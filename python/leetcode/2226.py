import math
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(m: int) -> int: # counter number of childs with m candies
            if m == 0:
                return True
            return sum([c // m for c in candies]) >= k
        max_ = max(candies)
        l, r = 0, max_

        res = -math.inf

        while l <= r:
            m = l + (r-l) // 2

            if check(m):
                l = m + 1
                res = max(res, m)
            else:
                r = m - 1

        return res


if __name__ == "__main__":
    candies = [2,5]
    k = 11
    print(Solution().maximumCandies(candies, k))



