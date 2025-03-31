from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        if k == 1 or k == N:
            return 0
        ww = [weights[i]+weights[i+1] for i in range(N-1)]
        ww.sort()
        i = k - 1
        return sum(ww[-i:]) - sum(ww[:i])