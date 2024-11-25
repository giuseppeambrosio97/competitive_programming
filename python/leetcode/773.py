from typing import List, Tuple
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """T(n)=O(6!)."""
        def locate_0(boardn: List[List[int]]) -> Tuple[int,int]: 
            for i in range(2):
                for j in range(3):
                    if boardn[i][j] == 0:
                        return (i,j)

        def ng(boardn: List[List[int]]) -> List[List[List[int]]]:
            i,j = locate_0(boardn)
            moves = [(0,1), (0,-1), (1,0), (-1,0)]
            res = []
            for ii,jj in moves:
                r = i + ii
                c = j + jj
                if 0 <= r < 2 and 0 <= c < 3:
                    new_board = [[n for n in row]for row in boardn]
                    new_board[r][c], new_board[i][j] = new_board[i][j], new_board[r][c]
                    res.append(new_board)

            return res
    
        q = deque([(board, 0)])
        visited = set([str(board)])
        final = str([[1,2,3],[4,5,0]])

        while q:
            boardn, dp = q.popleft()
            if str(boardn) == final:
                return dp
            for new_board in ng(boardn):
                if str(new_board) not in visited:
                    visited.add(str(new_board))
                    q.append((new_board, dp+1))

        return -1 

if __name__ == '__main__':
    board = [[4,1,2],[5,0,3]]
    a = Solution().slidingPuzzle(board)
    print(a)
