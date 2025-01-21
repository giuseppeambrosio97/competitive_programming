from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """O(n)=T(n)=S(n)."""
        n = len(height)
        lmax, rmax = [0]*n, [0]*n
        for i in range(n):
            lmax[i] = max(lmax[i-1], height[i]) if i!=0 else height[0]
            r = n-i-1
            rmax[r] = max(rmax[r+1], height[r]) if r!=n-1 else height[n-1]

        trapped = 0
        for i in range(n):
            cap = min(lmax[i], rmax[i])
            trapped += max(cap-height[i], 0)
        return trapped



if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Solution().trap(height)