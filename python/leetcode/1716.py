class Solution:
    def totalMoney(self, n: int) -> int:
        d,r = divmod(n,7)

        t1 = 7*(d*(d+1)//2+d*3) if d else 0
        t2 = sum(range(d+1,d+1+r))
        return t1+t2


if __name__ == "__main__":
    n = 10
    print(Solution().totalMoney(n))