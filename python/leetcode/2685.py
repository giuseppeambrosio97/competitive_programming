from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)

        for u,v in edges:
            G[u].append(v)
            G[v].append(u)


        visited = set()
        comp2nodes = defaultdict(list)
        
        def dfs(node, compid):
            visited.add(node)
            comp2nodes[compid].append(node)
            for nei in G[node]:
                if nei not in visited:
                    dfs(nei, compid)


        for node in range(n):
            if node not in visited:
                dfs(node, len(comp2nodes))
        
        res = 0
        for cidx, comps in comp2nodes.items():
            edges = sum([len(G[node]) for node in comps])
            if edges == len(comps) * (len(comps) - 1):
                res += 1
        
        return res
    
if __name__ == "__main__":
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
    print(Solution().countCompleteComponents(n,edges))