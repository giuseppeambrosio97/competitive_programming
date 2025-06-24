from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        R, C = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or j < 0 or i >= R or j >= C:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "T" # tmp to T
            for rr, cc in [(1,0),(-1,0),(0,1), (0,-1)]:
                dfs(i+rr,j+cc)
        
        for i in range(R):
            for k in [0,C-1]:
                if board[i][k] == 'O':
                    dfs(i,k)
        for j in range(C):
            for k in [0,R-1]:
                if board[k][j] == 'O':
                    dfs(k,j)
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    from pprint import pprint
    pprint(board)
