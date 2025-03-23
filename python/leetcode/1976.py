from collections import defaultdict
import heapq
import math
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        G = defaultdict(list)
        for u, v, w in roads:
            G[u].append((w,v))
            G[v].append((w,u))

        MOD = 10**9 + 7
        min_heap = [(0,0)] # (cost, nodeid)
        min_cost = [math.inf] * n
        path_cnt = [0]*n
        path_cnt[0] = 1

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            for nei_cost, nei in G[node]:
                if nei_cost+cost < min_cost[nei]:
                    min_cost[nei] = nei_cost+cost
                    path_cnt[nei] = path_cnt[node]
                    heapq.heappush(min_heap, (nei_cost+cost, nei))
                elif nei_cost + cost == min_cost[nei]:
                    path_cnt[nei] = (path_cnt[nei] + path_cnt[node]) % MOD

        return path_cnt[n-1]