from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def neighborhood(r,c) -> List[List[int]]:
            _neighborhood = []
            if r - 1 >= 0 and grid[r-1][c] == 1:
                _neighborhood.append([r-1,c])
            if r + 1 < m and grid[r+1][c] == 1:
                _neighborhood.append([r+1,c])
            if c - 1 >= 0 and grid[r][c-1] == 1:
                _neighborhood.append([r,c-1])
            if c + 1 < n and grid[r][c+1] == 1:
                _neighborhood.append([r,c+1])
            return _neighborhood
        
        def find_2(grid) -> List[List[int]]:
            cells_2 = []

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 2:
                        cells_2.append([r,c])
            return cells_2
        
        def check_if_no_fresh_orange(grid):
            fresh = False

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        fresh = True
            
            return not fresh
        
        def check_if_no_rotten_orange(grid):
            rotten = False

            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 2:
                        rotten = True
            
            return not rotten
        
        def repr(r,c):
            return f"{r},{c}"

        if check_if_no_fresh_orange(grid):
            return 0
        
        if check_if_no_rotten_orange(grid):
            return -1
        


        
        cells_2 = find_2(grid)

        q = deque([(cell_2, 0) for cell_2 in cells_2])
        to_visit = set([repr(r,c) for r in range(m) for c in range(n) if grid[r][c] != 0])
        res = 0
        while q:
            node, level = q.popleft()
            res = max(res,level)
            if repr(node[0],node[1]) in to_visit:
                to_visit.remove(repr(node[0],node[1]))

            for node_ in neighborhood(node[0],node[1]):
                if repr(node_[0],node_[1]) in to_visit:
                    to_visit.remove(repr(node_[0],node_[1]))
                    q.append((node_,level+1))

        if len(to_visit) > 0:
            return -1
        
        return res



if __name__ == '__main__':
    grid = [[2,2],[1,1],[0,0],[2,0]]
    s = Solution().orangesRotting(grid)
    print(s)