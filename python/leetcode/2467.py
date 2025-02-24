from collections import defaultdict
import math
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        T = defaultdict(list)

        for u,v in edges:
            T[u].append(v)
            T[v].append(u)

        def dfs_bob(node: int, parent: int, path: List[int]):
            if node == 0:
                return path
            
            for nei in T[node]:
                if nei != parent:
                    path.append(nei)
                    a = dfs_bob(nei, node, path)
                    if a:
                        return a
                    path.pop()
    
        bob_path = dfs_bob(bob, -1, [bob])

        i = 0
        while i < len(bob_path) // 2:
            amount[bob_path[i]] = 0
            i += 1

        if len(bob_path) % 2 == 1:
            amount[bob_path[len(bob_path)//2]] //= 2

        
        res = [-math.inf]
        def dfs_alice(node: int, parent: int, csum: int):
            if len(T[node]) == 1 and T[node][0] == parent:
                res[0] = max(res[0], csum+amount[node])
                return
            
            for nei in T[node]:
                if nei != parent:
                    dfs_alice(nei, node, csum+amount[node])
        
        dfs_alice(0,-1, 0)

        return res[0]


if __name__ == "__main__":
    edges = [[0,2],[0,4],[1,3],[1,2]]
    bob = 1
    amount = [3958,-9854,-8334,-9388,3410]
    print(Solution().mostProfitablePath(edges, bob, amount))