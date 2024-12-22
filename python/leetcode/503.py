from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """O(n^2)"""
        # n = len(nums)
        # res = [-1]*n
        # for i in range(n):
        #     j = (i + 1) % n
        #     while j != i:
        #         if nums[j] > nums[i]:
        #             res[i] = nums[j]
        #             break
        #         j += 1
        #         j %= n
        # return res
        """O(n) using monothonic stack"""
        n = len(nums)
        res = [-1]*n
        stack = []
        for r in range(2*n-1,-1,-1):
            rmod = r % n
            while stack and stack[-1] <= nums[rmod]:
                stack.pop()
            if r < n and stack:
                res[rmod] = stack[-1]
            stack.append(nums[rmod])
        return res


if __name__ == '__main__':
    nums = [2,2,5,4]
    Solution().nextGreaterElements(nums)