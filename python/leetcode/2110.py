from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            while l < r and prices[l] - prices[r]  != r - l:
                l += 1
            res += (r-l+1)
        return res 
    
if __name__ == "__main__":
    prices = [3,2,1,4]
    print(Solution().getDescentPeriods(prices))