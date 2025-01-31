from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_id = 2
        m, n = len(grid), len(grid[0])
        id_to_island_size = defaultdict(int)
        moves = [(1,0), (-1,0), (0,1), (0,-1)] 
        visited = set()

        def dfs(r, c):
            grid[r][c] = island_id
            id_to_island_size[island_id] += 1
            for rr, cc in moves:
                rr, cc = r+rr, c+cc
                if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1 and (rr, cc) not in visited:
                    visited.add((rr,cc))
                    dfs(rr,cc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r,c)
                    island_id += 1

        res = -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:

                    island_ids_set = set()
                    for rr, cc in moves:
                        rr, cc = r+rr, c+cc
                        if 0 <= rr < m and 0 <= cc < n:
                            island_ids_set.add(grid[rr][cc])
                    v = 1
                    for idx in island_ids_set:
                        v += id_to_island_size[idx]
                    res = max(res, v)
        return res if res != -1 else m*n




if __name__ == "__main__":
    grid = [
        [1, 0], 
        [0, 1],
    ]
    print(Solution().largestIsland(grid))
