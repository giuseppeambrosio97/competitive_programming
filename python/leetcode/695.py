import math
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int):
            cnt = 1
            visited.add((r, c))
            for rr, cc in moves:
                rr, cc = r + rr, c + cc
                if (
                    0 <= rr < m
                    and 0 <= cc < n
                    and (rr, cc) not in visited
                    and grid[rr][cc] == 1
                ):
                    cnt += dfs(rr, cc)
            return cnt

        max_ = -math.inf
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_ = max(max_, dfs(r,c))
        
        return max_ if max_ != -math.inf else 0



if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    t = Solution().maxAreaOfIsland(grid)
    print(t)
