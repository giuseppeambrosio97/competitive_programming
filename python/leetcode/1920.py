from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        M = 1000
        for i in range(len(nums)):
            nums[i] = (nums[i]+M*(nums[nums[i]] % M))
        for i in range(len(nums)):
            nums[i] //= M
        return nums