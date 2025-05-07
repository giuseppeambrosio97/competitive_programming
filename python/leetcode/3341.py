import heapq
import math
from typing import List, Tuple

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R , C = len(moveTime), len(moveTime[0])
        q = [(0,0,0)] # (r,c,time)

        def ng(r: int,c: int) -> List[Tuple[int]]:
            mvs = [(1,0),(-1,0),(0,1),(0,-1)]
            ngs = []
            for rr,cc in mvs:
                if 0 <= r+ rr < R and 0 <= c + cc < C:
                    ngs.append((r+rr,c+cc))
            return ngs
        
        visited = set()
        best = math.inf

        while q:
            t,r,c = heapq.heappop(q)

            if r == R-1 and c == C-1:
                best = min(t,best)

            for nr, nc in ng(r,c):
                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(q,(max(t,moveTime[nr][nc])+1,nr,nc))
        return best


if __name__ == "__main__":
    moveTime = [[27,85],[22,53]]
    print(Solution().minTimeToReach(moveTime))
    