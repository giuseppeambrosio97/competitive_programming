"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"val: {self.val}"


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # if not node:
        #     return None
        # s = [node]
        # h = {}
        # while s:
        #     a = s.pop()
        #     h[a] = Node(val=a.val)
        #     for child in a.neighbors:
        #         if child and child not in h:
        #             s.append(child)

        # s = [node]
        # visited = set()
        # while s:
        #     a = s.pop()
        #     h[a].neighbors = [h[child] for child in a.neighbors]

        #     for child in a.neighbors:
        #         if child and child not in visited:
        #             visited.add(child)
        #             s.append(child)

        # return h[node]
        """Recursive."""
        # h = {}

        # def dfsclone(node: Optional[Node]):
        #     if node in h:
        #         return h[node]
            
        #     copy = Node(val=node.val)
        #     h[node] = copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfsclone(nei))
        #     return copy
        
        # return dfsclone(node) if node else None
        """Iterative one step"""
        if not node:
            return None

        s = [node]
        h = {}
        h[node] = Node(val=node.val)

        while s:
            a = s.pop()

            for nei in a.neighbors:
                if nei not in h:
                    h[nei] = Node(val=nei.val)
                    s.append(nei)
                h[a].neighbors.append(h[nei])
        
        return h[node]

if __name__ == "__main__":
    print({Node(): Node()}.keys())
