import math
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sevents = sorted(events)
        n = len(sevents)
        
        def bs(l:int, target: int)->int:
            ll, rr = l, n
            while ll < rr:
                m = ll + (rr-ll) // 2
                if sevents[m][0] >= target:
                    rr = m
                else:
                    ll = m + 1
            return ll
        
        suffix_max = [0]*n
        max_ = -math.inf
        for i in range(n-1, -1, -1):
            suffix_max[i] = max(max_, sevents[i][2])
            max_ = max(max_, suffix_max[i])
        
        for i in range(n):
            j = bs(i, sevents[i][1]+1)
            if j < n:
                max_ = max(max_,sevents[i][2]+suffix_max[j])

        return max_
    
if __name__ == "__main__":
    events = [[1,3,2],[4,5,2],[2,4,3],[2,4,5]]
    Solution().maxTwoEvents(events)