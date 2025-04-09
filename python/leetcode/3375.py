from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1

        cnt = 0
        for a in sorted(set(nums), key=lambda x: -x):
            if a > k:
                cnt += 1
            else:
                return cnt
        return cnt