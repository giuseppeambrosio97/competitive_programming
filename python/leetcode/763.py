from collections import Counter, defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        tomatch = Counter(s)
        n = len(s)
        l = 0
        windowcnt = defaultdict(int)
        res = []
        for r in range(n):
            windowcnt[s[r]] += 1
            if windowcnt[s[r]] == tomatch[s[r]]:
                del windowcnt[s[r]]
            
            if len(windowcnt) == 0:
                res.append(r-l+1)
                l = r + 1
        return res