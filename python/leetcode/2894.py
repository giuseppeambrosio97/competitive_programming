class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        TOT = n*(n+1) // 2
        div_ = sum([i for i in range(1,n+1) if i % m == 0])
        notdiv_ = TOT - div_
        return notdiv_ - div_
