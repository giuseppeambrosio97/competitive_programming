"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List, Optional


class Node:
    def __init__(
        self,
        val=0,
        isLeaf=False,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def check(
            startrow: int, endrow: int, startcol: int, endcol: int
        ) -> Optional[int]:
            """
            Return 1 if there are all one
            Return 0 if there are all zeros
            Return None otherwise
            """
            firstval = grid[startrow][startcol]
            for r in range(startrow, endrow):
                for c in range(startcol, endcol):
                    if grid[r][c] != firstval:
                        return None
            return firstval

        def dfs(startrow: int, endrow: int, startcol: int, endcol: int) -> "Node":
            v = check(startrow, endrow, startcol, endcol)
            if v is not None:
                return Node(v, True)

            midrow, midcol = (startrow + endrow) // 2, (startcol + endcol) // 2
            return Node(
                val=0,
                isLeaf=False,
                topLeft=dfs(startrow, midrow, startcol, midcol),
                topRight=dfs(startrow, midrow, midcol, endcol),
                bottomLeft=dfs(midrow, endrow, startcol, midcol),
                bottomRight=dfs(midrow, endrow, midcol, endcol),
            )

        return dfs(0, len(grid), 0, len(grid[0]))


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]
    print(Solution().construct(grid))
