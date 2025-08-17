

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n:
            return 1.0
        dp = [0.0]*(n+maxPts+1)
        for i in range(k,n+1):
            dp[i] = 1.0
        EPS = 1 / maxPts
        winsum = n - k + 1
        for i in range(k-1,-1,-1):
            dp[i] = EPS*winsum
            winsum += dp[i] - dp[i+maxPts]

        return dp[0]


if __name__ == "__main__":
    n = 21
    k = 17
    maxp = 10
    print(Solution().new21Game(n,k,maxp))