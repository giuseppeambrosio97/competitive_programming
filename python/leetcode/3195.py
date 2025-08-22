from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        mr, MR = R, 0
        mc, MC = C, 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    mr, MR = min(mr,r), max(MR,r)
                    mc, MC = min(mc,c), max(MC,c)
        
        return (MR-mr+1)*(MC-mc+1)
