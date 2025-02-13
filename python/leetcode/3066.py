import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0
        while nums[0] < k:
            min_ = heapq.heappop(nums)
            max_ = heapq.heappop(nums)
            heapq.heappush(nums, min_*2 + max_)
            cnt += 1    
        return cnt
