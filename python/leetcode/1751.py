import bisect
from functools import lru_cache
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [e[0] for e in events]
        N = len(events)

        @lru_cache(maxsize=None)
        def dp(i: int, left: int):
            if i >= N or left <= 0:
                return 0
            dont_take = dp(i+1,left) # don't take

            next_id = bisect.bisect_right(starts,events[i][1], lo=i)
            take = events[i][2] + dp(next_id,left-1)

            return max(take,dont_take)
            
        return dp(i=0,left=k)

if __name__ == "__main__":
    events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    k = 2
    print(Solution().maxValue(events, k))