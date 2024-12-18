from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """O(n^2)"""
        # res = [0]*len(prices)
        # for i, p in enumerate(prices):
        #     g = 0
        #     for j in range(i+1, len(prices)):
        #         if prices[j] <= p:
        #             g = prices[j]
        #             break
        #     res[i] = prices[i] - g
        # return res
        """O(n)"""
        n = len(prices)
        s = []
        res = [0]*n
        for i in range(n-1, -1, -1):
            while s and s[-1] > prices[i]:
                s.pop()
            res[i] = prices[i] - (s[-1] if s else 0)
            s.append(prices[i])
        
        return res


if __name__ == '__main__':
    prices = [10,1,1,6]
    s = Solution().finalPrices(prices)
    print(s)