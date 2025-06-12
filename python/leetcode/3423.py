import math
from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        N = len(nums)
        max_ = -math.inf
        for i in range(N):
            max_ = max(max_, abs(nums[i]-nums[(i+1)%N]))
        return max_