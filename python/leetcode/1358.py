from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = defaultdict(int)
        res = 0
        l = 0
        n = len(s)

        for r in range(n):
            cnt[s[r]]+=1

            while len(cnt) >= 3:
                res += (n-r)
                cnt[s[l]]-=1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l += 1
        return res