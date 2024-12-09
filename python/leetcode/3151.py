from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if not (nums[i] & 1) ^ (nums[i+1] & 1):
                return False
        return True

