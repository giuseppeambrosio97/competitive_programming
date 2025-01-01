import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bs(l: int, r: int):
            m = l + ((r-l) // 2)

            vm = nums[m]
            vml = nums[m-1] if m > 0 else -math.inf 
            vmr = nums[m+1] if m < len(nums) - 1 else -math.inf

            if vm > vmr:
                if vm > vml:
                    return m
                return bs(0, m-1)
            else:
                return bs(m+1, r)

        return bs(0, len(nums)-1)