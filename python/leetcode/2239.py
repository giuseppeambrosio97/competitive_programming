from collections import Counter
import math
from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        c = Counter([n for n in nums])
        min_ = math.inf
        for a in c:
            min_ = min(min_, abs(a))

        return min_ if min_ in c else -min_