from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = [el for row in grid for el in row]

        mo = -1
        for el in a:
            if mo >= 0 and mo != el % x:
                return -1
            mo = el % x
        a.sort()

        m = len(a) // 2
        res = 0
        for i in range(len(a)):
            if a[m] > a[i]:
                res += (a[m]-a[i]) // x
            else:
                res += (a[i]-a[m]) // x
        
        return res
