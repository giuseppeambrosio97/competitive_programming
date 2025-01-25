from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        snums = sorted(nums)
        buckets = {}
        num_to_bucket = {}
        num_buckets = 0

        l = 0
        for r in range(1,n+1):
            if r == n or snums[r] - snums[r-1] > limit:
                buckets[num_buckets] = deque(snums[l:r])
                for a in snums[l:r]:
                    num_to_bucket[a] = num_buckets
                num_buckets += 1
                l = r

        buckets[num_buckets] = deque(snums[l:r+1])
        for a in snums[l:r+1]:
            num_to_bucket[a] = num_buckets
        
        return [buckets[num_to_bucket[a]].popleft() for a in nums]


if __name__ == '__main__':
    nums = [1,7,6,18,2,1]
    limit = 3
    Solution().lexicographicallySmallestArray(nums, limit)