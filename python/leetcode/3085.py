from collections import Counter
from functools import lru_cache


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        freqs = sorted([c for c in freq.values()])

        @lru_cache(maxsize=None)
        def dp(i,j):
            if freqs[j] - freqs[i] <= k:
                return 0
            
            return min(
                freqs[i]+dp(i+1,j),
                freqs[j]-freqs[i]-k+dp(i,j-1)
            )

        return dp(0,len(freqs)-1)

if __name__ == "__main__":
    word = "aabcaba"
    k = 0
    print(Solution().minimumDeletions(word, k))