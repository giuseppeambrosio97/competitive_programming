import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        csum = 0
        best = math.inf

        while l <= r and r < n:
            while r < n and csum < target:
                csum += nums[r]
                r += 1
            
            while l <= r and csum >= target:
                best = min(best,r - l)
                csum -= nums[l]
                l += 1
        
        return best if best != math.inf else 0




if __name__ == '__main__':
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    s = Solution().minSubArrayLen(target, nums)
    print(s)