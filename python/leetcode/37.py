from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def box_id(r,c):
            return (r // 3)*3 + c // 3
        empty_cells = [(r,c) for r in range(9) for c in range(9) if board[r][c] == "."]
        rows, cols, boxes = [[0]*10 for _ in range(9)], [[0]*10 for _ in range(9)], [[0]*10 for _ in range(9)]
        # fill used values in each rows, cols, boxes
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                vv = int(board[r][c])
                rows[r][vv] = 1
                cols[c][vv] = 1
                boxes[box_id(r,c)][vv] = 1
        def bk(i):
            if i == len(empty_cells):
                return True
            r,c = empty_cells[i]
            for v in range(1,10):
                if rows[r][v] or cols[c][v] or boxes[box_id(r,c)][v]:
                    continue
                rows[r][v] = cols[c][v] = boxes[box_id(r,c)][v] = 1
                board[r][c] = str(v)
                if bk(i+1):
                    return True
                rows[r][v] = cols[c][v] = boxes[box_id(r,c)][v] = 0
                board[r][c] = "."
            return False
        bk(0)


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    Solution().solveSudoku(board)
