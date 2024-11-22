from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dct = {}

        max_ = 0

        for vi in matrix:
            if vi[0]:
                vi = [0 if a else 1 for a in vi]
            vit = tuple(vi)
            dct[vit] = dct.get(vit, 0) + 1
            max_ = max(max_, dct[vit])
        return max_


if __name__ == "__main__":
    matrix = [
        [0, 0, 0],
        [0, 0, 1],
        [1, 1, 0],
    ]
    a = Solution().maxEqualRowsAfterFlips(matrix)
    print(a)
