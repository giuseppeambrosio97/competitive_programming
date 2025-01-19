class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # cnt = 0
        # for _ in range(32):
        #     xi = x & 1
        #     yi = y & 1
        #     cnt += xi ^ yi
        #     x >>=  1
        #     y >>= 1
        # return cnt
        xor = x ^ y
        cnt = 0
        while xor > 0:
            cnt += xor & 1
            xor >>= 1
        return cnt
