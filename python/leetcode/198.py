from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # @lru_cache(None)
        # def dp(i: int):
        #     if i >= n:
        #         return 0
        #     return max(nums[i] + dp(i+2), dp(i+1))
        # return dp(0)

        prev1, prev2 = 0,0

        for n in nums:
            curr = max(prev1, n + prev2)
            prev1 = curr
            prev2 = prev1

        return prev1
            