from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque([((0,0), 0)])
        visited = set([(0,0)])

        def ng(r:int,c: int):
            moves = [(0,-1), (0,1), (-1,0), (1,0)]
            res = []
            for mv in moves:
                rr, cc = r + mv[0], c + mv[1]
                if 0 <= rr < m and 0 <= cc < n and (rr,cc) not in visited:
                    res.append((rr,cc))
            return res


        while q:
            a, l = q.popleft()
            if a == (m-1,n-1):
                return l
            childs = ng(a[0],a[1])
            while childs:
                rr,cc = childs.pop()
                if (rr,cc) not in visited:
                    if grid[rr][cc] == 0:
                        q.appendleft(((rr,cc),l))
                    else:
                        q.append(((rr,cc),l+1))
                    visited.add((rr,cc))

if __name__ == '__main__':
    grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    t = Solution().minimumObstacles(grid)
    print(t)