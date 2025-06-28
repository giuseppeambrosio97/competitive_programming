from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ss = [(i,n)for i, n in enumerate(nums)]
        ss.sort(key=lambda x: -x[1])
        return [n for idx, n in sorted(ss[:k])]

