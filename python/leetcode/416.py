# from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        target = sum(nums)

        if target & 1:
            return False
        
        target //= 2
        dp = set([0])

        for i in range(N-1,-1,-1):
            nextDP = set()
            for t in dp:
                tt = nums[i] + t
                if tt == target:
                    return True
                if tt not in dp:
                    nextDP.add(nums[i]+t)
            dp = dp.union(nextDP)
        return target in dp
        

        
        # @lru_cache(maxsize=None)
        # def dp(i: int, csum: int = 0) -> bool:
        #     if i >= N:
        #         return False
            
        #     if target - csum == csum:
        #         return True
            
        #     return dp(i+1, csum+nums[i]) or dp(i+1, csum)
        # return dp(0)
    
if __name__ == "__main__":
    print(Solution().canPartition([1,5,11,5]))