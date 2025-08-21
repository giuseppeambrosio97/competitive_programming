from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])

        histmatrix = [[1 if a == "1" else 0 for a in matrix[0]]]
        for r in range(1,R):
            hist = []
            for c in range(C):
                hist.append(histmatrix[r - 1][c] + 1 if matrix[r][c] == "1" else 0)
            histmatrix.append(hist)

        def maxarea(hist: List[int]) -> int:
            N = len(hist)
            lh, stack = [0]*N, []
            for i, h in enumerate(hist):
                while stack and stack[-1][0] >= h:
                    stack.pop()
                if stack:
                    lh[i] = stack[-1][1] + 1
                stack.append((h,i))
            rh, stack = [N-1]*N, []
            for i, h in enumerate(reversed(hist)):
                ii = N - i - 1
                while stack and stack[-1][0] >= h:
                    stack.pop()
                if stack:
                    rh[ii] = stack[-1][1] - 1
                stack.append((h,ii))
            
            res = -1
            for i, h in enumerate(hist):
                res = max(res,h*(rh[i]-lh[i]+1))
            return res

        res = -1
        for hist in histmatrix:
            res = max(res, maxarea(hist))
        return res


if __name__ == "__main__":
    matrix = [["1"]
    ]
    print(Solution().maximalRectangle(matrix))
