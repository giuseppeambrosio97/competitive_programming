class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            mm = m * m
            if mm < x:
                l = m + 1
                res = m
            elif mm > x:
                r = m - 1
            else:
                return m
        return res


if __name__ == "__main__":
    s = Solution().mySqrt(6)
    print(s)
