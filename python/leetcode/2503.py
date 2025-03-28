import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        qs = sorted(queries)

        PQ = [(grid[0][0],0,0)]
        visited = set([(0,0)])

        DP = {} # q -> res mapping
        cnt = 0

        for query in qs:
            if query not in DP:
                while PQ and query > PQ[0][0]:
                    _, r, c = heapq.heappop(PQ)
                    cnt+=1
                    moves = [(1,0),(-1,0), (0,1), (0,-1)]
                    for rr,cc in moves:
                        rr = r+rr
                        cc = c+cc
                        if 0 <= rr < m and 0 <= cc < n and (rr,cc) not in visited:
                            visited.add((rr,cc))
                            heapq.heappush(PQ, (grid[rr][cc],rr,cc))
                DP[query] = cnt

        res = []
        for query in queries:
            res.append(DP[query])
        return res


        

if __name__ == "__main__":
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    print(Solution().maxPoints(grid, queries))