from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)

        pre_mapping = defaultdict(set)
        visited = set()

        def dfs(u: int, src: int):
            if u not in visited:
                visited.add(u)
                pre_mapping[src].add(u)
                for nei in graph[u]:
                    dfs(nei, src)

        for u in range(numCourses):
            visited = set()
            dfs(u,u)

        return [v in pre_mapping[u] for u,v in queries]
                