from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def id_to_rc(id):
            # Convert cell number to (row, col)
            quot, rem = divmod(id - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        n = len(board)
        visited = set()
        Q = deque([(1, 0)])  # (cell, moves)
        target = n*n

        while Q:
            curr, moves = Q.popleft()
            if curr == target:
                return moves
            for roll in range(1, 7):
                next_cell = curr + roll
                if next_cell > target:
                    continue
                r, c = id_to_rc(next_cell)
                dest = board[r][c] if board[r][c] != -1 else next_cell
                if dest not in visited:
                    visited.add(dest)
                    Q.append((dest, moves + 1))
        return -1
