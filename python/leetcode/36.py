from typing import List, Tuple
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(x: List[str]) -> bool:
            cnt = Counter(x)
            del cnt["."]
            if len(cnt) == 0:
                return True
            if cnt.most_common()[0][1] > 1:
                return False
            return True

        for i in range(9):
            row_i = board[i]
            if not validate(row_i):
                return False
        for i in range(9):
            col_i = [board[j][i] for j in range(9)]
            if not validate(col_i):
                return False

        def sub_cube_id(i: int, j: int) -> Tuple[int, int]:
            sr = (i // 3) * 3
            sc = (i % 3) * 3
            offset_r = j // 3
            offset_c = j % 3
            return (sr + offset_r, sc + offset_c)

        for i in range(9):
            sub_cube_i = []
            for j in range(9):
                ids = sub_cube_id(i, j)
                sub_cube_i.append(board[ids[0]][ids[1]])
            if not validate(sub_cube_i):
                return False

        return True


if __name__ == "__main__":
    s = Solution().isValidSudoku(
        # [
        #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        # ]
        # [
        #     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
        #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
        #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        #     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        # ]
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )

    print(s)
