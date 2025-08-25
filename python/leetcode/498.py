from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        res = []
        for s in range(R+C-1):
            diag = []
            r = 0 if s < C else s - C + 1
            c = s if s < C else C - 1
            while r < R and c >= 0:
                diag.append(mat[r][c])
                r += 1
                c -= 1
            res.extend(diag if s & 1 else diag[::-1])
        return res

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(Solution().findDiagonalOrder(mat))
