from typing import List
from operator import itemgetter
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        S(n) = O(k)
        T(n) = O(nlogn)
        """
        sorted_pairs = sorted(list(zip(nums1, nums2)),key=itemgetter(1), reverse=True)
        heap = []
        sum_n1 = 0
        best = 0
        for n1, n2 in sorted_pairs:
            heapq.heappush(heap, n1)
            sum_n1 += n1

            if len(heap) > k:
                sum_n1 -= heapq.heappop(heap)
            
            if len(heap) == k:
                best = max(best, sum_n1*n2)

        return best


if __name__ == "__main__":
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    s = Solution().maxScore(nums1=nums1, nums2=nums2, k=k)
    print(s)
