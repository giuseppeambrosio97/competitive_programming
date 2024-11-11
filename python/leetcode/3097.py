import math
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bnums = [
            [i for i, bi in enumerate(bin(a)[2:][::-1]) if bi == "1"] for a in nums
        ]
        cnt = [0 for _ in range(32)]
        if k == 0:
            return 1
        l, r = 0, 0
        best = math.inf
        curr_v = 0
        while l <= r and r < n:
            ## expand
            while r < n and curr_v < k:
                for i in bnums[r]:
                    if cnt[i] == 0:
                        curr_v += 2**i
                    cnt[i] = cnt[i] + 1
                r += 1
            ## restrict
            while l < r and curr_v >= k:
                best = min(best, r - l)
                for i in bnums[l]:
                    if cnt[i] == 1:
                        curr_v -= 2**i
                    cnt[i] = cnt[i] - 1
                l += 1

        return best if best != math.inf else -1

if __name__ == '__main__':
    nums = [1,2,32,21]
    k = 55
    s = Solution().minimumSubarrayLength(nums,k)
    print(s)