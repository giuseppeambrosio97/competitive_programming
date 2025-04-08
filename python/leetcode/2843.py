class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_sym(n: int) -> bool:
            ns = str(n)
            if len(ns) & 1:
                return False
            ns2 = len(ns) // 2

            return sum([int(a) for a in ns[:ns2]]) == sum([int(a) for a in ns[ns2:]])

        cnt = 0
        for n in range(low, high+1):
            if is_sym(n):
                cnt+=1
        return cnt