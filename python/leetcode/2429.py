class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """O(log2(n))"""
        def cnt_bints(n: int):
            r = 0
            while n > 0:
                r += n & 1
                n = n >> 1
            return r
        
        n1, n2 = cnt_bints(num1), cnt_bints(num2)

        if n1 == n2:
            return num1

        res = num1
        i = 0
        ## if there more 1 bits in num1 so starting from num1 be have to flip to 0 the first n1-n2 1 bits of num1
        ## so basically we are removing 1 bits from num1 (to have the same number of bits with num2)
        ## if there more 1 bits in num2 so starting from num1 he have to flip to 1 the first n2-n1 0 bits of num1
        ## so basically we are adding 1 bit in num1 (to have the same number of bits with num2)
        while n1 != n2:
            if n1 > n2 and res & (1<<i):
                n1 -= 1
                res ^= (1 << i)
            if n1 < n2 and not res & (1<<i):
                n2 -= 1
                res |= (1 << i)
            i += 1

        return res

if __name__ == '__main__':
    num1 = 5
    num2 = 7
    print(Solution().minimizeXor(num1, num2))