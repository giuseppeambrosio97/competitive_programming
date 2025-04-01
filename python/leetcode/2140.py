from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        #@lru_cache(None)
        #def dp(i: int):
        #    if i >= N:
        #        return 0
        #    earn, skip = questions[i]
        #    return max(earn+dp(i+skip+1), dp(i+1))
        #return dp(0)

        def get_i(i: int):
            return cache[i] if i < N else 0

        cache = [0]*N
        for i in reversed(range(N)):
            earn, skip = questions[i]
            cache[i] = max(
                earn+get_i(i+skip+1), 
                get_i(i+1)
            )
        print(cache)
        return cache[0]
