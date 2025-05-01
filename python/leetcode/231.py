import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and 2**int(math.log(n,2)) == n