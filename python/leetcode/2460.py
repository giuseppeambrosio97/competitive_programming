from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        idx = 0
        for i in range(n):
            if nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx+=1
        return nums