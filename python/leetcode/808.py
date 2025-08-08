from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500:
            return 1
        ops = [100, 75, 50, 25, 0]
        @lru_cache(maxsize=None)
        def dp(A,B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0 and B > 0:
                return 1
            if A > 0 and B <= 0:
                return 0
            res = 0
            for i in range(4):
                res += dp(A-ops[i], B-ops[4-i])*0.25
            return res
        
        return dp(n,n)

if __name__ == "__main__":
    n = 4500
    print(Solution().soupServings(n))