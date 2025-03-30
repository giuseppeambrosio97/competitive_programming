from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        I = sorted([(s,-e) for s,e in intervals])

        res = 1
        cstart, cend = I[0]
        cend = -cend

        for start, end in I[1:]:
            end = -end
            if cstart > start or end > cend:
                cstart, cend = start, end
                res += 1
        
        return res
