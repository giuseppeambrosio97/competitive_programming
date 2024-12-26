from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """O(nglogng + nslogns + min(ns,ng))"""
        g, s = sorted(g), sorted(s)
        ng, ns = len(g), len(s)

        cnt = 0
        j = 0
        for i in range(ns):
            if j < ng and s[i] >= g[j]:
                cnt += 1
                j += 1
            if j >= ng:
                return cnt
        
        return cnt


if __name__ == "__main__":
    g = [10,9,8,7]
    s = [5,6,7,8]
    t = Solution().findContentChildren(g, s)
    print(t)
        