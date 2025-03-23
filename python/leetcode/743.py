from collections import defaultdict
import heapq
import math
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(list)
        for u,v,w in times:
            G[u].append((w,v))

        minheap = [(0,k)] # (cost, node(starting from k))
        mincost = [math.inf] * (n+1)
        mincost[k] = 0 

        while minheap:
            cost, node = heapq.heappop(minheap)
            for neicost, nei in G[node]:
                if mincost[nei] > neicost+cost:
                    mincost[nei] = neicost+cost
                    heapq.heappush(minheap, (neicost+cost, nei))
        
        res = -math.inf
        for i in range(1,n+1):
            if mincost[i] == math.inf:
                return -1
            res = max(res, mincost[i])
        
        return res
            