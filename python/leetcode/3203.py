from collections import defaultdict
from math import ceil
from typing import Dict, List, Tuple


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_adj_list(edges: List[List[int]]) -> Dict[int, List[int]]:
            G = defaultdict(list)
            for u,v in edges:
                G[u].append(v)
                G[v].append(u)
            return G
        
        G1 = build_adj_list(edges1)
        G2 = build_adj_list(edges2)

        def farthest_node(node: int, parent: int, G: Dict[int, List[int]], distance: int, res: List[int]):
            """Put in res list the pair (node, distance)"""
            if res[1] < distance:
                res[0] = node
                res[1] = distance
            
            for nei in G[node]:
                if nei != parent:
                    farthest_node(nei, node, G, distance+1, res)

        def diameter(G: Dict[int, List[int]]) -> int:
            res1, res2 = [0,0], [0,0]
            farthest_node(node=0, parent=-1, G=G,distance=0,res=res1)
            farthest_node(node=res1[0], parent=-1, G=G,distance=0,res=res2)
            return res2[1]


        d1 = diameter(G1)
        d2 = diameter(G2)

        return max(d1, d2, ceil(d1/ 2)+ceil(d2/ 2)+1)