from functools import lru_cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def get_next(r, c, d):
            nextmove = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
            dr, dc = nextmove[d]
            return (r + dr, c + dc)

        @lru_cache(maxsize=None)
        def dp(r, c, d, target, canchange):
            rr, cc = get_next(r, c, d)
            if rr < 0 or rr >= R or cc < 0 or cc >= C or grid[rr][cc] != target:
                return 0
             
            res = dp(rr,cc,d,2-target, canchange)
            if canchange:
                res = max(
                    res,
                    dp(rr,cc,(d+1)%4,2-target,False)
                )
            return res + 1
        max_ = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] != 1:
                    continue
                for d in range(4):
                    max_ = max(max_, dp(r, c, d, 2, True)+1)
        return max_


if __name__ == "__main__":
    grid = [
        [2, 2, 2, 2, 2],
        [2, 0, 2, 2, 0],
        [2, 0, 1, 1, 0],
        [1, 0, 2, 2, 2],
        [2, 0, 0, 2, 2],
    ]
    print(Solution().lenOfVDiagonal(grid))
