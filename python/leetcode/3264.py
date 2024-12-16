import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        pq = [(n,i) for i,n in enumerate(nums)]
        heapq.heapify(pq)
        for _ in range(k):
            a,idx = heapq.heappop(pq)
            heapq.heappush(pq, (a*multiplier,idx))
            nums[idx] = a*multiplier
        return nums