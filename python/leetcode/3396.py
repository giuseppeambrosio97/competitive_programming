from collections import defaultdict
import math
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        m = defaultdict(int)

        N = len(nums)

        for i in range(N-1, -1, -1):
            if m[nums[i]] == 0:
                m[nums[i]]+=1
            else:
                return math.ceil((i + 1) / 3)
                
        
        return 0