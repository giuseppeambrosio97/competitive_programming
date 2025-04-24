from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        curr = 1
        l = 0
        for r in range(len(nums)):
            curr *= nums[r]
            while curr >= k:
                curr //= nums[l]
                l += 1
            res += (r - l + 1)
        return res


if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    Solution().numSubarrayProductLessThanK(nums, k)