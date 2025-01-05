from collections import defaultdict
import math
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """T(s,t)=O(n+m)"""
        m, n = len(s), len(t)
        if m < n:
            return ""
        target_count = Counter(t)
        window_count = defaultdict(int)
        l = 0
        is_good = 0
        best = math.inf
        res = (-1,-1)
        for r, char_r in enumerate(s):
            window_count[char_r] += 1
            if char_r in target_count and window_count[char_r] <= target_count[char_r]:
                is_good += 1
            while is_good == n:
                char_l = s[l]
                if best > r-l+1:
                    best = r-l+1
                    res = (l,r)
                window_count[char_l] -= 1
                if char_l in target_count and window_count[char_l] < target_count[char_l]:
                    is_good -= 1
                l += 1
        l, r = res
        return s[l:r+1]

if __name__ == '__main__':
    s = "bba"
    t = "ab"
    c = Solution().minWindow(s,t)
    print(c)