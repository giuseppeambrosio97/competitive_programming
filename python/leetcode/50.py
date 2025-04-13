class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        sign = 1 if n > 0 else 0

        n = abs(n)

        while n > 0:
            if n & 1:
                res *= x
            n //= 2
            x *= x


        return res if sign else 1 / res