from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)

        cnt = defaultdict(int)
        res = 1
        for r in range(n):
            cnt[s[r]] += 1
            if cnt[s[r]] >= 2:
                cnt = defaultdict(int)
                cnt[s[r]] = 1
                res+=1
    
        return res
