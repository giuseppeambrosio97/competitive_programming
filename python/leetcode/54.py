from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nr, nc = len(matrix), len(matrix[0])
        visited = [[0 for _ in range(nc)] for _ in range(nr)]
        
        res = []
        i = 0
        r,c = 0,-1
        currmove = "R"

        change = {
            "U": "R",
            "R": "D",
            "D": "L",
            "L": "U"
        }

        direction_to_move = {
            "U": (1,0),
            "R": (0,1),
            "L": (0,-1),
            "D": (-1,0)
        }

        while i < nc*nr:
            while True:
                rr,cc = direction_to_move[currmove]
                if r + rr < 0 or r + rr >= nr or c + cc < 0 or c + cc >= nc or visited[r+rr][c+cc]:
                    ## change move
                    break
                res.append(matrix[r+rr][c+cc])
                r = r + rr
                c = c + cc 
                visited[r][c] = 1
                i += 1

            currmove = change[currmove]
        
        return res 


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    t = Solution().spiralOrder(matrix)
    print(t)