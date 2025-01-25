from collections import defaultdict, deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        snums = sorted(nums)
        buckets = defaultdict(deque)
        buckets[0].appendleft(snums[0])
        num_to_bucket = {snums[0]: 0}

        for r in range(1,n):
            if snums[r] - snums[r-1] > limit:
                num_to_bucket[snums[r]] = len(buckets)
                buckets[len(buckets)].append(snums[r])
            else:
                buckets[len(buckets)-1].append(snums[r])
                num_to_bucket[snums[r]] = len(buckets) - 1

        return [buckets[num_to_bucket[a]].popleft() for a in nums]


if __name__ == '__main__':
    nums = [1,5,3,9,8]
    limit = 2
    Solution().lexicographicallySmallestArray(nums, limit)