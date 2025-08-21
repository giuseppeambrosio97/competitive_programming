from functools import lru_cache
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(r,c):
            if r == R or c == C or not matrix[r][c]:
                return 0
            return 1 + min(
                dfs(r,c+1),
                dfs(r+1,c),
                dfs(r+1,c+1)
            )

        res = 0
        for r in range(R):
            for c in range(C):
                res+=dfs(r,c)
        return res