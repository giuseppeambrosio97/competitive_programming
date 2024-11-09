from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        curmax_ = prices[-1]
        best = 0
        for i in range(n-2,-1,-1):
            best = max(best, curmax_ - prices[i])
            curmax_ = max(curmax_, prices[i])

        return best        


if __name__ == '__main__':
    s = Solution().maxProfit(prices=[1,2])
    print(s)