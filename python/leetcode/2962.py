from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        res = l = maxfreq = 0
        for r in range(len(nums)):
            if nums[r] == max_el:
                maxfreq += 1
            while maxfreq == k:
                if nums[l] == max_el:
                    maxfreq -= 1
                l += 1
            res += l
        return res