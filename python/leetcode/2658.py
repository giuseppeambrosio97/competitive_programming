from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        moves = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int):
            visited.add((r,c))
            cnt = grid[r][c]
            for rr,cc in moves:
                rr, cc = r+rr, c+cc
                if 0 <= rr < m and 0 <= cc < n and (rr,cc) not in visited and grid[rr][cc] > 0:
                    cnt += dfs(rr,cc)
            return cnt

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and (r,c) not in visited:
                    visited.add((r,c))
                    res = max(dfs(r,c), res)
        
        return res

if __name__ == "__main__":
    grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    print(Solution().findMaxFish(grid))
        