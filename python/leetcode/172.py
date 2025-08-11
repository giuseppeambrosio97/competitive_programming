class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 1
        while (c := n//5**i) > 0:
            res += c
            i += 1
        return res