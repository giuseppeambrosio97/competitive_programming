from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        entrance = tuple(entrance)
        def is_exit(r: int, c: int):
            if maze[r][c] == "+" or ((r,c) == entrance):
                return False            
            return r == 0 or r == m - 1 or c == 0 or c == n - 1

        def ng(r: int, c: int) -> List[List[int]]:
            ng_ = []
            if r - 1 >= 0 and maze[r-1][c] == ".":
                ng_.append([r - 1, c])
            if r + 1 < m and maze[r+1][c] == ".":
                ng_.append([r + 1, c])
            if c - 1 >= 0 and maze[r][c-1] == ".":
                ng_.append([r, c - 1])
            if c + 1 < n and maze[r][c+1] == ".":
                ng_.append([r, c + 1])
            return ng_

        q = deque([(entrance, 0)])
        visited = set([entrance])


        while q:
            (r, c), level = q.popleft()

            for r_, c_ in ng(r,c):
                
                if (r_,c_) not in visited:
                    if is_exit(r_,c_):
                        return level + 1
                    visited.add((r_, c_))
                    q.append(((r_, c_), level + 1))
            
        return  -1

if __name__ == "__main__":
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]

    s = Solution().nearestExit(maze=maze, entrance=entrance)
    print(s)
