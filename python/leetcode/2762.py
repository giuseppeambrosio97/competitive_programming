from typing import List
from collections import defaultdict



class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """O(n)"""
        m = defaultdict(int)
        l,r = 0, 0
        cnt = 0

        for r, nr in enumerate(nums):
            m[nr] += 1

            while abs(max(m) - min(m)) > 2:
                if m[nums[l]] == 1:
                    del m[nums[l]]
                else:
                    m[nums[l]] -= 1
                l += 1
            
            cnt += (r-l+1)
        
        return cnt


if __name__ == '__main__':
    # nums = [5,4,2,4]
    # nums = [6,1,6,1,6,1,6]
    # nums = [65,66,67,66,66,65,64,65,65,64]
    nums = [65,66,67,66,66,65,64]
    t = Solution().continuousSubarrays(nums)
    print(t)