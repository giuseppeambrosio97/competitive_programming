from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0 
        left = nums[0]

        smax = [0]*(N+1)
        for j in range(N-1, -1, -1):
            smax[j] = max(smax[j+1],nums[j])

        for j in range(N-1):
            if nums[j] > left:
                left = nums[j]
                continue
            res = max(
                res,
                (left-nums[j])*smax[j+1],
                0
            )

        return res