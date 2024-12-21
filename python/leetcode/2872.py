from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        dedges = defaultdict(list)
        for u, v in edges:
            dedges[u].append(v)
            dedges[v].append(u)

        res = [0]

        def dfs(curr: int, parent: int):
            _sum = 0

            for u in dedges[curr]:
                if u != parent:
                    _sum += dfs(u, curr)
                    _sum %= k
            _sum += values[curr]
            _sum %= k
            if _sum == 0:
                res[0] += 1
            return _sum
        dfs(0, -1)
        return res[0]


if __name__ == "__main__":
    n = 7
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    values = [3,0,6,1,5,2,1]
    k = 3
    t = Solution().maxKDivisibleComponents(n, edges, values, k)
    print(t)
