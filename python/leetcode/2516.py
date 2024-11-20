from collections import Counter
import math


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def is_good(cnt: Counter) -> bool:
            return len(cnt) == 3 and cnt.most_common()[2][1] >= k
        if k == 0:
            return 0
        cnt = Counter(s)
        if not is_good(cnt):
            return -1
        
        l,r, n = 0, 0, len(s)
        best = n + 1
        for r in range(n):
            cnt[s[r]] -= 1
            while not is_good(cnt):
                cnt[s[l]] += 1
                l += 1
            best = min(best, n - (r-l+1))
        return best





if __name__ == "__main__":
    s = "caccbbba"
    k = 1
    a = Solution().takeCharacters(s, k)
    print(a)
