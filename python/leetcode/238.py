from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        acc = 1
        for i in range(n - 1):
            acc *= nums[i]
            res[i+1] = acc

        acc = 1
        for i in range(n-1, 0, -1):
            acc *= nums[i]
            res[i-1] *= acc

        return res
        



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    # l -> r: [1,  1,  2, 6]
    # r -> l  [24, 12, 4, 1]
    # final ->[24, 12, 8, 6]
    Solution().productExceptSelf(nums)
