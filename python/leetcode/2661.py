from collections import defaultdict
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ## preprocess: need the coord of the cell with value arr[i]
        h = {}
        m,n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                h[mat[r][c]] = (r,c)
            
        hr = defaultdict(int)
        hc = defaultdict(int)
        for i, v in enumerate(arr):
            r,c = h[v]
            hr[r]+=1
            hc[c]+=1

            if hr[r] == n or hc[c] == m:
                return i 
