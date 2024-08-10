from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        DFS starting from node 0:
            if node is already visited do nothing

            for edge in dct:
                if edge[1] == node:
                    dfs(edge[0])
                else:
                    cnt++
                    dfs(edge[1])
        """
        dct = {i: [] for i in range(n)}

        for i in range(n-1):
            nodes = connections[i]
            dct[nodes[0]].append(nodes)
            dct[nodes[1]].append(nodes) 

        visited = set()
        cnt = 0

        def dfs(node: int):
            nonlocal cnt
            
            visited.add(node)
            
            for edge in dct[node]:
                if edge[1] == node:
                    if edge[0] not in visited:
                        dfs(edge[0])
                else:
                    if edge[1] not in visited:
                        cnt += 1
                        dfs(edge[1])

        dfs(0)
        return cnt


if __name__ == '__main__':
    n = 3
    connections = [[1,0],[2,0]]

    s = Solution().minReorder(n=n, connections=connections)

    print(s)