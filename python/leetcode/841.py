from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(i, rooms: List[List[int]]):
            if i in visited:
                return 
            visited.add(i)
            for node in rooms[i]:
                dfs(node, rooms)

        dfs(0, rooms)

        return len(visited) == len(rooms)

if __name__ == '__main__':
    print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))