
from functools import lru_cache
from typing import List


class Solution:

    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(i: int, csum: int):
            if i >= n:
                return 1 if csum == target else 0

            psum = dfs(i+1, csum + nums[i])
            nsum = dfs(i+1, csum - nums[i])
            return nsum + psum


        return dfs(0,0)
        
if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    t = Solution().findTargetSumWays(nums,target)
    print(t)
