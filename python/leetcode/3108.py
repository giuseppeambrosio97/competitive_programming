from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        default_and = ~0
        
        G = defaultdict(list)
        W = {}
        for u,v,w in edges:
            G[u].append(v)
            G[v].append(u)
            e = tuple(sorted([u,v]))
            W[e] = W.get(e, default_and) & w
        
        node2comp_id = {} # nodeid -> (compid)
        comp2and = {} # comp id value

        def dfs(node, compid):
            for nei in G[node]:
                e = tuple(sorted([node,nei]))
                comp2and[compid] = comp2and.get(compid, default_and) & W[e]             
                if nei not in node2comp_id:
                    node2comp_id[nei] = compid
                    dfs(nei,compid)

        for nodeid in range(n):
            if nodeid not in node2comp_id:
                compid = len(comp2and)
                node2comp_id[nodeid] = compid
                dfs(nodeid, compid)

        res = []
        for u,v in query:
            res.append(-1 if node2comp_id[u] != node2comp_id[v] else comp2and[node2comp_id[u]])
        return res
    
if __name__ == "__main__":
    n = 6
    edges = [[1,5,1],[4,3,3],[3,5,3],[1,0,1],[3,0,0]]
    query = [[0,2],[4,5],[5,1],[0,4],[0,1],[0,4],[4,2],[4,0]]
    print(Solution().minimumCost(n,edges,query))