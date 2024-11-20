class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     """Combinatorial math approach"""
    #     return math.comb(m + n - 2, n - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        """DP approach"""
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            dp[r][n - 1] = 1

        for c in range(n):
            dp[m - 1][c] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
 
        return dp[0][0]


if __name__ == "__main__":
    m, n = 3, 7
    s = Solution().uniquePaths(m, n)
    print(s)
