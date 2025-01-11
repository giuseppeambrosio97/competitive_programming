import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = 0
        res = -math.inf
        for n in nums:
            csum += n
            res = max(res, csum)
            if csum < 0:
                csum = 0
        return res

