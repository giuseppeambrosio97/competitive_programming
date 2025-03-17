from collections import defaultdict
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for n in nums:
            m[n]+=1

        for v in m.values():
            if v & 1:
                return False

        return True
