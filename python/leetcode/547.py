from typing import List, Set


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def neighborhood(i,  isConnected: List[List[int]]) -> Set[int]:
            return {j for j in range(0, len(isConnected)) if isConnected[i][j] == 1 and i != j}
        
        def dfs(node: int, isConnected: List[List[int]]):
            if node in visited:
                return
            
            visited.add(node)
            neighborhood_i = neighborhood(node, isConnected)

            nodes_to_visit = neighborhood_i - visited

            if nodes_to_visit:
                for node in nodes_to_visit:              
                    dfs(node, isConnected)
            


        n = len(isConnected)
        visited = set()
        cnt = 0

        for node in range(n):
            if node not in visited:  
                cnt += 1
            dfs(node, isConnected)

        return cnt


if __name__ == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))