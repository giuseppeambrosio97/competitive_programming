from collections import Counter
from functools import cache
from math import comb


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        num = list(map(int, num))
        TOT = sum(num)
        if TOT & 1:
            return 0
        TARGET = TOT // 2
        cnt = Counter(num)
        n = len(num)
        max_odd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, odd_cnt):
            # If the remaining positions cannot complete a legal placement, or the sum of the elements in the current odd positions is greater than the target value
            if odd_cnt < 0 or psum[pos] < odd_cnt or curr > TARGET:
                return 0
            if pos > 9:
                return int(curr == TARGET and odd_cnt == 0)
            even_cnt = (
                psum[pos] - odd_cnt
            )  # Even-numbered positions remaining to be filled
            res = 0
            for i in range(
                max(0, cnt[pos] - even_cnt), min(cnt[pos], odd_cnt) + 1
            ):
                # Place i of the current number at odd positions, and cnt[pos] - i at even positions
                ways = comb(odd_cnt, i) * comb(even_cnt, cnt[pos] - i) % MOD
                res += ways * dfs(pos + 1, curr + i * pos, odd_cnt - i)
            return res % MOD

        return dfs(0, 0, max_odd)
         