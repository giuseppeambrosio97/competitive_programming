from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(a0,a1,b0,b1,c0,c1):
            return abs((b0-a0)*(c1-a1)-(b1-a1)*(c0-a0))*0.5
    
        N = len(points)
        max_ = 0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    max_ = max(area(*points[i],*points[j],*points[k]),max_)
        return max_


if __name__ == "__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(Solution().largestTriangleArea(points))