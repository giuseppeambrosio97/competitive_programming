import heapq
import math
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(pq)
        cmax = max([nums[i][0] for i in range(len(nums))])
        res = [
            -math.inf,
            math.inf,
        ]

        while True:
            cmin, row, col = heapq.heappop(pq)
            if (cmax - cmin < res[1] - res[0]) or (
                cmax - cmin == res[1] - res[0] and cmin < res[0]
            ):
                res = [cmin, cmax]
            if col + 1 < len(nums[row]):
                nextv = nums[row][col + 1]
                heapq.heappush(pq, (nextv, row, col + 1))
                cmax = max(cmax, nextv)
            else:
                return res



if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    res = Solution().smallestRange(nums=nums)
    print(res)
