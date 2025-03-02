from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n

        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        
        cnt = 0
        for i in reversed(range(n)):
            if i < n-1 and ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1] + 1
            cnt += res[i]
        
        return cnt

if __name__ == "__main__":
    # ratings = [4,3,2,1]
    # ratings = [1,2,3,4]
    # ratings = [1,2,3,0,2,1]
    ratings = [1,0,2]
    Solution().candy(ratings)