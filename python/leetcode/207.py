
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        n = numCourses
        m = len(prerequisites)
        
        T(n) = n + m 
            for prerequisites is O(m)
            for counter is O(n)
            while q is O(n)
                and for graph[node] is O(m)

                -> but the outer loop run at most once for each node and the inner loop in total will process each edge ones
                so the overall time complexity is O(n+m)
        so the final time complexity is O(n+m)

        S(n) = O(n + m)
            counter -> O(n)
            graph -> O(n+m)
        """
        counter = [0]*numCourses
        graph = defaultdict(list)


        for after, before in prerequisites:
            counter[after] += 1
            graph[before].append(after)

        q = deque()

        for node, in_degree in enumerate(counter):
            if in_degree == 0:
                q.append(node)

        visited = 0

        while q:
            node = q.popleft()
            visited += 1

            for nei in graph[node]:
                counter[nei] -= 1
                if counter[nei] == 0:
                    q.append(nei)

        return visited == numCourses



if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().canFinish(numCourses, prerequisites))