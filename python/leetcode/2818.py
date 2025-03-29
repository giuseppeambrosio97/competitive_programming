import heapq
import math
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        prime_scores = []
        MOD = 10**9+7
        N = len(nums)

        for n in nums:
            cnt = 0
            for f in range(2,math.floor(math.sqrt(n))+1):
                if n % f == 0:
                    cnt += 1
                    while n % f == 0:
                        n //= f
            if n >= 2:
                cnt += 1
            prime_scores.append(cnt)

        lb = [-1]*N
        rb = [N]*N
        stack = []
        for idx, n in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < n: # stop until at leat equal or empty
                index = stack.pop()
                rb[index] = idx
            if stack:
                lb[idx] = stack[-1]
            stack.append(idx)

        MPQ = [(-n,idx) for idx, n in enumerate(nums)]
        heapq.heapify(MPQ)
        res = 1

        while k > 0:
            n, idx = heapq.heappop(MPQ)
            n = -n
            lf = idx - lb[idx]
            rf = rb[idx] - idx
            op = min(lf*rf,k)
            res = (res * pow(n,op,MOD)) % MOD
            k -= op
        return res


