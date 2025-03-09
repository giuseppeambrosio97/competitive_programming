from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        cnt = 0
        n = len(colors)

        for i in range(n):
            l = colors[(i-1)%n]
            r = colors[(i+1)%n]
            if colors[i] not in [l,r]:
                cnt +=1
        
        return cnt