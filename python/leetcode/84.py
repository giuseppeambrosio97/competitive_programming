from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        H = len(heights)
        lh = [0]*H
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][0] >= h:
                stack.pop()
            
            if stack:
                lh[i] = stack[-1][1]+1            
            stack.append((h,i))
        stack = []
        rh = [H-1]*H
        for r in range(H-1, -1, -1):
            while stack and stack[-1][0] >= heights[r]:
                stack.pop()
            
            if stack:
                rh[r] = stack[-1][1]-1
            stack.append((heights[r],r))
        res = -1
        for i in range(len(heights)):
            res = max(res, heights[i]*(rh[i]-lh[i]+1))
        return res
                
if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(Solution().largestRectangleArea(heights))