from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def cnt_digits(a: int) -> int:
            o = 0
            while a > 0:
                o += (a % 10)
                a //= 10
            return o

        cnt = defaultdict(int)
        max_ = -1
        for i in range(1,n+1):
            t = cnt_digits(i)
            cnt[t] += 1
            max_ = max(max_, cnt[t])
        
        return sum([1 for k,v in cnt.items() if v == max_])

