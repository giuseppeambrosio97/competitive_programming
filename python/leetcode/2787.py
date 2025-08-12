from functools import lru_cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0:
                return 1
            jx = j**x
            if jx > i:
                return 0
            
            use = dp(i-jx, j+1)
            notuse = dp(i, j+1)

            return (use + notuse ) % MOD

        return dp(n,1)

if __name__ == "__main__":
    n = 10
    x = 2
    print(Solution().numberOfWays(n,x))