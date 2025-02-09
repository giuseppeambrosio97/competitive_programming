from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        cnt = defaultdict(int)
        res = 0
        for i, n in enumerate(nums):
            v = i - n
            d[i] = v
            cnt[v] += 1
            if cnt[v] > 1:
                res += cnt[v] - 1
        n = len(nums)
        return n * (n-1) // 2 - res
