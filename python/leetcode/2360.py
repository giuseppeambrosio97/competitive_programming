from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        """
        T(n) = O(2n)
        S(n) = O(2n)
        """
        n = len(edges)
        visited = [False] * n
        res = -1

        for start in range(n):
            if not visited[start]:
                current_path = {}
                current_node = start
                steps = 0

                while current_node != -1:
                    if current_node in current_path:
                        cl = steps - current_path[current_node]
                        res = max(res, cl)
                        break

                    if visited[current_node]:
                        break
                
                    current_path[current_node] = steps
                    visited[current_node] = True
                    current_node = edges[current_node]
                    steps += 1
        return res



if __name__ == '__main__':
    edges = [-1,4,-1,2,0,4]
    print(Solution().longestCycle(edges))