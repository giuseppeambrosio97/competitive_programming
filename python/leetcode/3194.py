import heapq
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        avgs = []
        for i in range(n//2):
            heapq.heappush(avgs, (nums[i]+nums[n-i-1])/2)
        return avgs[0]