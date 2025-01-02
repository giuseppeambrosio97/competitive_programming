from typing import List, Set, Tuple

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        tovisit = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    tovisit.append((r,c))

        def dfs(r: int, c: int, visited: Set[Tuple[int, int]]):
            if (r in (-1, m) or c in (-1, n) or not grid[r][c] or (r,c) in visited):
                return
            visited.add((r,c))
            moves = [(r+1,c), (r-1,c), (r, c+1), (r,c-1)]
            for rr,cc in moves:
                dfs(rr,cc, visited)

        def cnt_components() -> int:
            visited = set()
            cnt = 0
            for r,c in tovisit:
                if grid[r][c] == 1 and  (r,c) not in visited:
                    dfs(r,c, visited)
                    cnt += 1
                    if cnt > 1:
                        return 2
            return cnt
                    
        if cnt_components() != 1:
            return 0

        for r,c in tovisit:
            grid[r][c] = 0
            if cnt_components() != 1:
                return 1
            grid[r][c] = 1

        return 2




if __name__ == "__main__":
    grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    t = Solution().minDays(grid)
    print(t)