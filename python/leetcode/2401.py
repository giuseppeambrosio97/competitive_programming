from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)

        res = 1
        mask = nums[0]

        for r in range(1, n):
            while mask & nums[r]:
                mask ^= nums[l]
                l += 1
            mask |= nums[r]
            res = max(res, r - l + 1)

        return res

