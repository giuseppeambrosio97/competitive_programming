from functools import lru_cache
from typing import List


class Solution:
    """O(n^2)"""
    # def canJump(self, nums: List[int]) -> bool:
        
    #     n = len(nums)
    #     @lru_cache(maxsize=None)
    #     def can(i: int):
    #         if i >= n - 1:
    #             return True
    #         if i + nums[i] >= n-1:
    #             return True
    #         for j in range(i+1, i+1+nums[i]):
    #             if can(j):
    #                 return True
    #         return False
    #     return can(0)
    
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, n in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i+n)
        return True

if __name__ == '__main__':
    nums = [1,2,3]
    tt = Solution().canJump(nums)
    print(tt)