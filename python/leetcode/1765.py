from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1]*n for _ in range(m)]

        q = deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    heights[r][c] = 0

        level = 1
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while q:
            level_size = len(q)
            for _ in range(level_size):
                r,c = q.popleft()
                
                for rr,cc in moves:
                    rr,cc=r+rr,c+cc
                    if (
                        0<= rr < m and 0<=cc<n and
                        heights[rr][cc] == -1
                    ):
                        heights[rr][cc] = level
                        q.append((rr,cc))
            level += 1
        return heights

