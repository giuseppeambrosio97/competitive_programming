from functools import lru_cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        at each step we can use the string "0"*zero (call it a) or "1"*one (call it b)

        we have to count the number of possible such strings with  low <= lenght <= high:

        if zero=1 and one=1 -> 2*(low) + 2*(low+1) + .... + 2*(high)
        """
        MOD = 10**9 + 7
    
        @lru_cache(maxsize=None)
        def dp(s: int):
            if s > high:
                return 0            
            cnt = 1 if low <= s else 0
            cnt += dp(s+one)
            cnt += dp(s+zero)
            return cnt % MOD

        return dp(0)



if __name__ == "__main__":
    low = 3
    high = 3
    zero = 1
    one = 1
    t = Solution().countGoodStrings(low, high, zero, one)
    print(t)
