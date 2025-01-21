from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2*nums[i]
                nums[i+1] = 0
        l = 0
        while l < n:
            if nums[l] == 0:
                r = l + 1
                while r < n and nums[r] == 0:
                    r += 1
                if r >= n:
                    break
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return nums

