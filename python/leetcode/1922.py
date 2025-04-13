import math


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow(x,n):
            res = 1
            while n > 0:
                if n & 1:
                    res = (res * x) % MOD
                n //= 2
                x = (x*x) % MOD
            return res

        even = math.ceil(n/2)
        odd = n // 2

        return (pow(5,even)*pow(4,odd) % MOD)

        