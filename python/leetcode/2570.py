from collections import defaultdict
import math
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(int)
        n1,n2 = len(nums1), len(nums2)
        res = []
        i1, i2 = 0,0
        while i1 < n1 or i2 < n2:
            idx1 = nums1[i1][0] if i1 < n1 else math.inf
            idx2 = nums2[i2][0] if i2 < n2 else math.inf
            if idx1 == idx2 and idx1 != math.inf and idx2 != math.inf:
                cnt[idx1]+= nums1[i1][1]
                cnt[idx1]+= nums2[i2][1]
                res.append([idx1, cnt[idx1]])
                i1+=1
                i2+=1
            if idx1 < idx2 and idx1 != math.inf:
                cnt[idx1] += nums1[i1][1]
                res.append([idx1,cnt[idx1]])
                i1 += 1
            if idx1 > idx2 and idx2 != math.inf:
                cnt[idx2]+=nums2[i2][1]
                res.append([idx2, cnt[idx2]])
                i2+=1
        return res 
                