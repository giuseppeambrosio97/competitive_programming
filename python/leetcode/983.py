from functools import lru_cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """O(n) top down"""
        # day_set = set(days) 
        # @lru_cache(maxsize=None)
        # def dp(currday: int):
        #     if currday > days[-1]:
        #         return 0
            
        #     if currday not in day_set:
        #         return dp(currday+1)
            
        #     d1 = dp(currday+1) + costs[0]
        #     d7 = dp(currday+7) + costs[1]
        #     d30 = dp(currday+30) + costs[2]
        #     return min(d1, d7, d30)
        
        # return dp(days[0])
        days_set = set(days)
        last_d = days[-1]
        dp = [0]*(last_d+1)
        for d in range(1,last_d+1):
            if d not in days_set:
                dp[d] = dp[d-1]
            else:
                dp[d] = min(
                    dp[max(0,d-1)] + costs[0],
                    dp[max(0,d-7)] + costs[1],
                    dp[max(0,d-30)] + costs[2],
                )
        return dp[last_d]


if __name__ == '__main__':
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    t = Solution().mincostTickets(days, costs)
    print(t)