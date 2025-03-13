import math
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def check(m: int) -> bool:
            diff = [0]*(n+1)
            for l,r,v in queries[:m+1]:
                diff[l] += v
                diff[r+1] -=v

            c = 0

            for i, a in enumerate(diff):
                c += a
                if i < n and c < nums[i]:
                    return False
            
            return True
        
        l, r = -1, len(queries)-1

        res = math.inf

        while l <= r:
            m = l + (r-l) // 2
            if check(m):
                res = min(res, m+1)
                r = m - 1
            else:
                l = m + 1
        return res if res != math.inf else -1


if __name__ == "__main__":
    nums = [0]
    queries = [[0,0,5],[0,0,1],[0,0,3],[0,0,2]]
    print(Solution().minZeroArray(nums,queries))