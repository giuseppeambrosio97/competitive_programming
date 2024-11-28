from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle.copy()
        n = len(dp)

        for i in range(n-2, -1, -1):
            cn = len(dp[i])
            for j in range(cn):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]


if __name__ == "__main__":
    triangle = [[-1],[2,3],[1,-1,-3]]
    t = Solution().minimumTotal(triangle)
    print(t)
