from bisect import bisect_left, bisect_right
import math
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N1, N2 = len(nums1), len(nums2)
        def count(cval: int) -> int:
            cnt = 0
            for x in nums1:
                if x > 0:
                    cnt += bisect_right(nums2, cval / x)
                elif x < 0:
                    cnt += N2 - bisect_left(nums2,math.ceil(cval / x))
                else: # x == 0
                    if cval >= 0:
                        cnt += N2
            return cnt

        low, high = -10**10-1, 10**10+1
        res = high

        while low < high:
            mid = (low+high) // 2
            if count(mid) >= k:
                res = mid
                high = mid
            else:
                low = mid + 1
        return res
