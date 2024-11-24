import math
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negativecnt = 0
        absmin = math.inf
        sum_ = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] < 0:
                    negativecnt += 1
                abs_ = abs(matrix[i][j])
                sum_ += abs_
                absmin = min(absmin, abs_)

        return sum_ if negativecnt % 2 == 0 else sum_ - absmin * 2


if __name__ == "__main__":
    matrix = [[2, 9, 3], [5, 4, -4], [1, 7, 1]]
    s = Solution().maxMatrixSum(matrix)
    print(s)
