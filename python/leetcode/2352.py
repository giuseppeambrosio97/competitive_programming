from typing import List
import collections

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Brutal force T(n) = n^3
        def equalPairs(self, grid: List[List[int]]) -> int:
            n = len(grid)
            count = 0
            for i in range(n):
                row = grid[i]
                for j in range(n):
                    col = [grid[r][j] for r in range(n)]
                    if row == col:
                        count += 1
            return count

        We can do better by using hashmap to save rows and cols occurrences
        """
        n = len(grid)
        rows_dct = collections.defaultdict(int)
        for i in range(n):
            rows_dct[",".join(map(str,grid[i]))] +=1

        cols_dct = collections.defaultdict(int)
        for j in range(n):
            col = [str(grid[i][j]) for i in range(n)]
            cols_dct[",".join(col)] += 1

        count = 0
        for col, col_frequency in cols_dct.items():
            count += rows_dct.get(col, 0) * col_frequency

        return count            




if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(Solution().equalPairs(grid))