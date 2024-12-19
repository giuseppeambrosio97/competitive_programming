from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """O(n)"""
        n = len(arr)
        nexti = 0
        cnt = 0
        for i in range(n):
            nexti = max(nexti, arr[i])
            if i == nexti:
                cnt += 1
                nexti = i + 1
        return cnt
        """O(3n)"""
        # n = len(arr)
        # pmax, smin = [0]*n, [0]*n
        # for i in range(n):
        #     pmax[i] = max(arr[i], pmax[i-1]) if i > 0 else arr[0]
        # for i in range(n-1, -1,-1):
        #     smin[i] = min(arr[i], smin[i+1]) if i < n - 1 else arr[-1]
        # cnt = 0
        # for i in range(n):
        #     if i == 0 or smin[i] > pmax[i-1]:
        #         cnt += 1
        # return cnt