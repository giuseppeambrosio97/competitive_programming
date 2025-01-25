from collections import defaultdict
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        snums = sorted(nums)
        n = len(snums)
        buckets = defaultdict(list)
        num_to_bucket = {}
        num_buckets = 0

        l = 0
        for r in range(1,n):
            if snums[r] - snums[r-1] > limit:
                buckets[num_buckets] = snums[l:r]
                for a in snums[l:r]:
                    num_to_bucket[a] = num_buckets
                num_buckets += 1
                l = r

        buckets[num_buckets] = snums[l:r+1]
        for a in snums[l:r+1]:
            num_to_bucket[a] = num_buckets

        bucket_id_to_current_idx_to_take = defaultdict(int)

        res = []
        for a in nums:
            bucket_id = num_to_bucket[a]
            if len(buckets[bucket_id]) == 1:
                res.append(a)
            else:
                res.append(buckets[bucket_id][bucket_id_to_current_idx_to_take[bucket_id]])
                bucket_id_to_current_idx_to_take[bucket_id] += 1
        
        return res


if __name__ == '__main__':
    nums = [1,7,6,18,2,1]
    limit = 3
    Solution().lexicographicallySmallestArray(nums, limit)