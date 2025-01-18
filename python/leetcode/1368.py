import math
from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """S(m,n)=O(m*n), T(m,n)=O(4*m*n*log(4*m*n))."""
        m, n = len(grid), len(grid[0])

        if m*n == 1:
            return 0

        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        pq = [(0,0,0)] # (cost,r,c) starting from the top left corner
        min_cost = [[math.inf]*n for _ in range(m)]
        # min_cost[0][0] = 0
        while pq:
            cost, r, c = heapq.heappop(pq)
            #try all possible moves
            for d, (rr,cc) in enumerate(moves):
                rr, cc = r+rr, c+cc
                if 0<=rr<m and 0 <=cc<n: ## check if the move is valid
                    newcost = cost + (d + 1 != grid[r][c])
                    if min_cost[rr][cc] > newcost:
                        min_cost[rr][cc] = newcost
                        heapq.heappush(pq, (newcost, rr,cc))
        
        return min_cost[m-1][n-1]

if __name__ == '__main__':
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    print(Solution().minCost(grid))