from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bs = set(banned)
        s = 0
        cnt = 0
        for i in range(1,n+1):
            if i not in bs and i + s <= maxSum:
                cnt += 1
                s += i
        return cnt
