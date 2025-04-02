from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        res = -1
        left = nums[0]
        for j in range(N-1):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j+1, N):
                res = max(
                    res,
                    (left-nums[j])*nums[k],
                    0
                )
        return res