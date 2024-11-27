from typing import List
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        edges = {i: [i + 1] for i in range(n)}

        def shortest():
            q = deque([(0, 0)])
            visited = set([0])
            while q:
                a, l = q.popleft()
                if a == n - 1:
                    return l
                for child in edges[a]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, l + 1))
            

        res = []
        for i, j in queries:
            edges[i].append(j)
            r = shortest()
            res.append(r)
        return res


if __name__ == "__main__":
    n = 6
    queries = [[1, 4], [0, 2]]
    t = Solution().shortestDistanceAfterQueries(n, queries)
    print(t)
