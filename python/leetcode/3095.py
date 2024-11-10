import math
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = math.inf
        for i in range(n):
            for j in range(i, n):
                orbit = 0
                for r in range(i,j+1):
                    orbit |= nums[r]

                if orbit >= k:
                    best = min(best, j-i+1)
        return -1 if best == math.inf else best