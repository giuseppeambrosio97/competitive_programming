from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] == j - i:
                j += 1
            if nums[j-1] == nums[i]:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[j-1]}")
            i = j
        return res
        