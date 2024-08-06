from typing import List
from operator import itemgetter

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=itemgetter(1))

        i, n = 0, len(points)
        cnt = 0
        while i < n:
            arrow_x = points[i][1]
            cnt += 1
            j = i + 1
            while j < n and arrow_x >= points[j][0]:
                j += 1
            i = j     
        return cnt

if __name__ == '__main__':
    points = [[1,2],[3,4],[5,6],[7,8]]
    s = Solution().findMinArrowShots(points=points)
    print(s)