from collections import Counter


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        c01 = (a ^ b) & ~c

        c02 = (a & b) & ~c

        c11 = (~a) & (~b) & c

        def count1(x: int) -> int:
            return Counter(bin(x)[2:])["1"]

        return count1(c11) + count1(c01) + count1(c02) * 2


if __name__ == "__main__":
    a = 2
    b = 6
    c = 5
    a = Solution().minFlips(a, b, c)
    print(a)
