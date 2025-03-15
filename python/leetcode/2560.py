from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(c: int) -> bool:
            i, cnt = 0,0

            while i < n and cnt != k:
                if nums[i] <= c:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            
            return cnt == k

        l, r = min(nums), max(nums)

        res = 0

        while l <= r:
            m = l+(r-l)//2

            if check(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res