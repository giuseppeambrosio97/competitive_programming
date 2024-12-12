import heapq
from typing import List
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            a = heapq.heappop(gifts)
            if -a == 1:
                return len(gifts) + 1
            heapq.heappush(gifts, -math.floor(math.sqrt(-a)))
        return sum([-g for g in gifts])
        

if __name__ == '__main__':
    gifts = [25,64,9,4,100]
    k = 4
    t = Solution().pickGifts(gifts,k)
    print(t)