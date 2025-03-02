from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1] + 1
        
        return sum(res)

if __name__ == "__main__":
    # ratings = [4,3,2,1]
    # ratings = [1,2,3,4]
    # ratings = [1,2,3,0,2,1]
    ratings = [1,0,2]
    Solution().candy(ratings)