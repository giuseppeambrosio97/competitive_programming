from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        """O(nw0*nt + nw0*words)"""
        nw0, nt = len(words[0]), len(target)

        cnt = []
        for i in range(nw0):
            cnt.append(defaultdict(int))
            for chi in words:
                cnt[i][chi[i]] += 1     

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            """# starting from the index of words i in order to create target[j:]"""
            if nw0 - i < nt - j:
                return 0
            if j >= nt:
                return 1
            return (cnt[i][target[j]]*dp(i+1, j+1) + dp(i+1, j)) % (10**9+7)
                
        return dp(0,0)


if __name__ == "__main__":
    words = ["acca", "bbbb", "caca"]
    target = "aba"
    t = Solution().numWays(words, target)
    print(t)
