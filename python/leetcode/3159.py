from collections import defaultdict
from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        mapping = defaultdict(list)

        for idx, n in enumerate(nums):
            if n == x:
                mapping[x].append(idx)
        
        res = []
        OCC = len(mapping[x])
        for q in queries:
            res.append(
                -1 if q > OCC else mapping[x][q-1]
            )
        return res
