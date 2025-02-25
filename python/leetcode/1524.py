from collections import defaultdict
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        psum = [0]*(n+1)

        for i in range(1,n+1):
            psum[i] = psum[i-1] + arr[i-1]
        
        res = 0
        counter = defaultdict(int)
        counter[0] = 1
        for i in range(1, n+1):
            parity = psum[i] & 1
            res += counter[parity ^ 1]
            counter[parity] += 1
            res %= MOD
        return res


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    print(Solution().numOfSubarrays(arr))