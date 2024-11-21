from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [["1" for _ in range(n)] for _ in range(m)]

        for g0, g1 in guards:
            grid[g0][g1] = "G"
        for w0, w1 in walls:
            grid[w0][w1] = "W"

        def mv_up(r, c):
            rpp = r - 1
            while rpp >= 0 and grid[rpp][c] != "W" and grid[rpp][c] != "G":
                grid[rpp][c] = "0"
                rpp -= 1

        def mv_l(r, c):
            cpp = c - 1
            while cpp >= 0 and grid[r][cpp] != "W" and grid[r][cpp] != "G":
                grid[r][cpp] = "0"
                cpp -= 1

        def mv_r(r, c):
            cpp = c + 1 
            while cpp < n and grid[r][cpp] != "W" and grid[r][cpp] != "G":
                grid[r][cpp] = "0"
                cpp += 1

        def mv_down(r, c):
            rpp = r + 1 
            while rpp < m and grid[rpp][c] != "W" and grid[rpp][c] != "G":
                grid[rpp][c] = "0"
                rpp += 1

        for g0,g1 in guards:
            mv_up(g0,g1)
            mv_l(g0,g1)
            mv_r(g0,g1)
            mv_down(g0,g1)

        cnt = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    cnt += 1
        return cnt



if __name__ == "__main__":
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    a = Solution().countUnguarded(m, n, guards, walls)
    print(a)
