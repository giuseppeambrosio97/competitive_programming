import math
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cmax = -math.inf
        res = -math.inf
        for i in range(len(values)-1):
            cmax = max(cmax, values[i]+i)
            res = max(res, cmax+values[i+1]-i-1)
        
        return res



if __name__ == '__main__':
    values = [8,1,5,2,6]
    t = Solution().maxScoreSightseeingPair(values)
    print(t)