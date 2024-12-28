from functools import lru_cache
import math
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        intervalsum = [0] * (n-k+1)
        
        j = n - k
        csum = sum(nums[j:])
        intervalsum[-1] = csum
        for j in range(n-k-1,-1,-1):
            csum = csum + nums[j] - nums[j+k]
            intervalsum[j] = csum

        @lru_cache(maxsize=None)
        def dp(i: int, j: int):
            if j <= 0:
                return 0, []
            if i >= len(intervalsum):
                return -math.inf, []
            ## take the subarray i
            takesum, takeidxs = dp(i+k, j-1)
            takesum += intervalsum[i]
            takeidxs = [i] + takeidxs

            nottakesum, nottakeidxs = dp(i+1,j)
            
            if takesum >= nottakesum:
                return takesum, takeidxs
            else:
                return nottakesum, nottakeidxs
        
        return dp(0,3)[1]


if __name__ == '__main__':
    nums=[1,2,1,2,6,7,5,1]
    k=2
    t = Solution().maxSumOfThreeSubarrays(nums, k)
    print(t)
