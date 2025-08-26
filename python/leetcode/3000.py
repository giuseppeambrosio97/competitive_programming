import math
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        md = max(math.sqrt(d[0]*d[0] + d[1]*d[1]) for d in dimensions)
        ma = -1
        for d0,d1 in dimensions:
            if md == math.sqrt(d0*d0 + d1*d1):
                ma = max(ma, d0*d1)
        return ma