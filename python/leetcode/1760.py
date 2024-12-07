from math import ceil
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def cnt_opts(n: int, v: int):
            return ceil(n / v)-1
        
        def is_good(candidate: int) -> bool:
            left = maxOperations
            for a in nums:
                left -= cnt_opts(a,candidate)
                if left < 0:
                    return False
            return True
        l,r = 1, max(nums)
        while l < r:
            m = l + ((r-l) // 2)
            if is_good(m):
                r = m
            else:
                l = m + 1
        return l



if __name__ == '__main__':
    nums = [9, 10, 13]
    ### 9 -> 3,6 -> 3,3,3
    ### 10 -> 3,7-> 3,3,4 -> 3,3,3,1
    ### 11 -> 3,8 -> 3,3,5 -> 3,3,3,2
    ### 12 -> 3,9 -> 3,3,6 -> 3,3,3,3
    ### 13 -> 3,10 -> 3,3,7 -> 3,3,3,4 -> 3,3,3,3,1
    maxOperations = 2
    t = Solution().minimumSize(nums, maxOperations)
    print(t)