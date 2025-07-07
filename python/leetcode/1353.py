
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        T(n) = 
            nlogn   // sorting
            n       // max L
            L*nlogn // main loop
        """
        sevents = sorted(events)
        cnt = 0
        N = len(events)
        L = max([e for _,e in sevents])
        pq = []
        idx = 0
        for day in range(sevents[0][0], L+1):
            while idx < N and sevents[idx][0] <= day:
                heapq.heappush(pq, sevents[idx][1])
                idx += 1 

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                cnt += 1
        return cnt
        

if __name__ == "__main__":
    events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    print(Solution().maxEvents(events))