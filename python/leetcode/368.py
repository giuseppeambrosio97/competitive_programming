from functools import lru_cache
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        
        @lru_cache(maxsize=None)
        def dfs(i):
            if i == N:
                return []

            res = [nums[i]]

            max_ = []
            for j in range(i+1, N):
                if nums[j] % nums[i] == 0:
                    resj = dfs(j)
                    if len(max_) < len(resj):
                        max_ = resj
            return res + max_

        max_ = []
        for i in range(N):
            tmp = dfs(i)
            if len(max_) < len(tmp):
                max_ = tmp
        return max_
        
        @lru_cache(maxsize=None)
        def dfs(i, prev):
            if i == N:
                return []
            
            res = dfs(i+1,prev) # skip nums[i]

            if nums[i] % prev == 0:
                tmp = [nums[i]] + dfs(i+1,nums[i])
                res = tmp if len(res) < len(tmp) else res
            return res
        
        return dfs(0,1)

