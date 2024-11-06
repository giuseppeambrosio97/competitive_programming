from typing import List
import math

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def onebitcount(num: int) -> int:
            cnt = 0
            while num > 0:
                cnt += num & 1
                num >>= 1
            return cnt
        
        n = len(nums)
        
        if n == 1:
            return True
        
        r = 0
        prev_ones = onebitcount(nums[0])
        max_ = nums[0]
        min_ = nums[0]
        parts = []
        while r < n:
            onesr = onebitcount(nums[r])
            if onesr == prev_ones:
                max_ = max(max_, nums[r])
                min_ = min(min_, nums[r])
                r += 1
            else:
                parts.append((min_,max_))
                max_ = nums[r]
                min_ = nums[r]
            prev_ones = onesr
        parts.append((min_,max_))
        i = 0
        while i < len(parts) and i + 1 < len(parts):
            if parts[i][1] >= parts[i+1][0]:
                return False
            i += 1
        return True
            


if __name__ == '__main__':
    print(Solution().canSortArray([2,28,9]))