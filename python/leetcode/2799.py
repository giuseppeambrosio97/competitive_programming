from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        
        N = len(nums)
        res = 0
        cntr = defaultdict(int)
        l = 0
        for r in range(N):
            cntr[nums[r]] += 1
            if len(cntr) == target:
                res += (N-r)
                while l <= r and len(cntr) == target:
                    cntr[nums[l]] -= 1
                    if cntr[nums[l]] == 0:
                        del cntr[nums[l]]
                    if len(cntr) == target:
                        res += (N-r)
                    l += 1
        return res
    
if __name__ == "__main__":
    nums = [5,5,5,5]
    print(Solution().countCompleteSubarrays(nums))