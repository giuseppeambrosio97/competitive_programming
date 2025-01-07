from collections import defaultdict, deque
import math
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {"red": defaultdict(list), "blue": defaultdict(list)}
        for u,v in redEdges:
            graph["red"][u].append(v)

        for u,v in blueEdges:
            graph["blue"][u].append(v)

        res = [-1]*n

        def shortest():
            q = deque([(0,0,None)]) # (node, distance, prevcolor)
            visited = set() # track visited (node, color)
            while q:
                for _ in range(len(q)):
                    node, distance, prevcolor = q.popleft()
                    if res[node] == -1:
                        res[node] = distance
                    for color in ["red", "blue"]:
                        if color != prevcolor:
                            for v in graph[color][node]:
                                if (v, color) not in visited:
                                    visited.add((v,color))
                                    q.append((v, distance+1, color))

        shortest()
                            
        return [a if a != math.inf else -1 for a in res ]


if __name__ == '__main__':
    n = 5
    redEdges = [[0,1],[1,2],[2,3],[3,4]]
    blueEdges = [[1,2],[2,3],[3,1]]
    t = Solution().shortestAlternatingPaths(n, redEdges, blueEdges)
    print(t)