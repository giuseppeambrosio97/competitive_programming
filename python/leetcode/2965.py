from collections import defaultdict
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        """
        T(n^2)=O(n^2), S(n^2)=O(n^2).
        """
        cnt = defaultdict(int)
        n = len(grid)
        values = set(range(1,n*n+1))

        res = [0,0]

        for r in range(n):
            for c in range(n):
                if grid[r][c] in values:
                    values.remove(grid[r][c])
                cnt[grid[r][c]]+=1
                if cnt[grid[r][c]] == 2:
                    res[0] = grid[r][c]
        res[1] = next(iter(values))    
        return res
                    