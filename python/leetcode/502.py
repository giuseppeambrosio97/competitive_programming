import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        taken = 0
        capitalsorted = sorted([(c,idx) for idx,c in enumerate(capital)])

        profitsheap = []
        res = w
        while k > 0:
            while taken < n and capitalsorted[taken][0] <= res:
                c, idx = capitalsorted[taken]
                heapq.heappush(profitsheap, (-profits[idx], idx))
                taken += 1
            if not profitsheap:
                return res
            _, idx = heapq.heappop(profitsheap)
            res += profits[idx]
            k -= 1
        
        return res