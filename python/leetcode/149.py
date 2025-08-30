from collections import defaultdict
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        def slope(x1,y1,x2,y2):
            if x2-x1 == 0:
                return math.inf
            return (y2-y1) / (x2-x1)
        res = 0
        for i in range(N):
            counter = defaultdict(int)
            for j in range(i+1,N):
                m = slope(points[i][0],points[i][1], points[j][0],points[j][1])
                counter[m]+=1
                res = max(res,counter[m])
        return res+1


if __name__ == "__main__":
    points = [[3,3],[1,4]]
    print(Solution().maxPoints(points))