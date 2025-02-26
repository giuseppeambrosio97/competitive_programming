import math
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum, minsum = -math.inf, math.inf
        max_runningsum, min_runningsum = 0, 0
        for n in nums:
            max_runningsum += n
            min_runningsum += n
            maxsum = max(maxsum, max_runningsum)
            minsum = min(minsum, min_runningsum)
            max_runningsum = max(0, max_runningsum)
            min_runningsum = min(0, min_runningsum)
        return max(abs(maxsum), abs(minsum))