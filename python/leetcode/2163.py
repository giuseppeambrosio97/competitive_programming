import math
from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        K = N // 3


        # preprocess -> build right max sum
        minpq, rsum, rmaxsum = [], 0, [0]*N

        for i in range(N-1, K-1, -1):
            heapq.heappush(minpq, nums[i])
            rsum += nums[i]
            if len(minpq) > K:
                rsum -= heapq.heappop(minpq)
            if len(minpq) == K:
                rmaxsum[i] = rsum
        
        # compute min-diff by traversing left part (0 -> to 2k-1)
        maxpq, lsum, mindiff = [], 0, math.inf
        
        for i in range(2*K):
            heapq.heappush(maxpq, -nums[i])
            lsum += nums[i]
            if len(maxpq) > K:
                lsum += heapq.heappop(maxpq)
            if len(maxpq) == K and i+1 < N:
                mindiff = min(mindiff, lsum - rmaxsum[i+1])
        
        return mindiff

if __name__ == "__main__":
    nums = [7,9,5,8,1,3] 
    print(Solution().minimumDifference(nums))