from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        l = 0
        n = len(colors)
        cnt = 0

        for r in range(0, n+k-1):
            if colors[r%n] == colors[(r-1)%n]:
                l = r
            ll = r-l+1
            if ll == k:
                cnt += 1
            if ll >= k:
                l += 1
        return cnt
    

if __name__ == "__main__":
    colors = [0,1,0,0,1,0,1]
    k = 6
    print(Solution().numberOfAlternatingGroups(colors, k)) 