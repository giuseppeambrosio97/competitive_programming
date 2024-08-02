from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for el in nums:
            heapq.heappush(heap, (-el, str(el)))

        kthlargest = None
        for i in range(k):
            kthlargest = heapq.heappop(heap)

        return int(kthlargest[1])
    


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4], 3))