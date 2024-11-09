class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1) + 1 , len(word2) + 1
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = i

        for j in range(m):
            dp[0][j] = j

        for i in range(1, n):
            for j in range(1, m):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[n - 1][m - 1]


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"
    s = Solution().minDistance(word1, word2)
    print(s)
