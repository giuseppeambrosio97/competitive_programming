from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        used = set()
        N1, N2 = len(nums1), len(nums2)
        pq = [(nums1[0]+nums2[0], 0,0)]

        res = []
        while True:
            _, i1, i2 = heapq.heappop(pq)
            used.add((i1,i2))
            res.append((nums1[i1],nums2[i2]))
            if len(res) == k:
                return res
            i1pp = i1+1
            if (i1pp,i2) not in used and i1pp < N1:
                heapq.heappush(pq, (nums1[i1pp]+nums2[i2], i1pp,i2))
                used.add((i1pp,i2))
            i2pp = i2+1
            if (i1, i2pp) not in used and i2pp < N2:
                heapq.heappush(pq, (nums1[i1]+nums2[i2pp], i1,i2pp))
                used.add((i1,i2pp))


if __name__ == "__main__":
    nums1 = [1,2,4,5,6]
    nums2 = [3,5,7,9]
    k = 20
    print(Solution().kSmallestPairs(nums1,nums2,k))