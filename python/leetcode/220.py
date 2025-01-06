import bisect
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        """
        T(n)=O(n(4logk))
        remove -> logk
        bisect left/right -> logk
        bisect isort -> logk
        """
        # slist = []
        # for i, n in enumerate(nums):
        #     l = bisect.bisect_left(slist, n-valueDiff)
        #     r = bisect.bisect_right(slist, n+valueDiff)
        #     if r != l:
        #         return True
        #     bisect.insort(slist, n)

        #     if len(slist) > indexDiff:
        #         slist.remove(nums[i-indexDiff])
        # return False
        buckets = {}
        bucket_size = valueDiff + 1

        for i,n in enumerate(nums):
            bucket_id = n // bucket_size

            if bucket_id in buckets:
                return True
            
            if bucket_id - 1 in buckets and n - buckets[bucket_id-1] <= valueDiff:
                return True
            if bucket_id + 1 in buckets and buckets[bucket_id+1] - n <= valueDiff:
                return True
            
            buckets[bucket_id] = n
            
            if i >= indexDiff:
                del buckets[nums[i-indexDiff] // bucket_size]

        return False




if __name__ == "__main__":
    nums = [8, 7, 15, 1, 6, 1, 9, 15]
    indexDiff = 1
    valueDiff = 3
    res = Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
    print(res)
