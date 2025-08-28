from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])

        for s in range(R+C-1):
            r = 0 if s >= R else R - 1 - s
            c = 0 if s < R else s - R + 1
            diag = []
            while 0 <= r < R and 0 <= c < C:
                diag.append(grid[r][c])
                r += 1
                c += 1
            r = 0 if s >= R else R - 1 - s
            c = 0 if s < R else s - R + 1
            for v in sorted(diag, reverse=s < R):
                grid[r][c] = v
                r += 1
                c += 1
        return grid
            



if __name__ == "__main__":
    grid = [
        [1,7,3],
        [9,8,2],
        [4,5,6],
    ]
    print(Solution().sortMatrix(grid))