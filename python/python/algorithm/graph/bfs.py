from typing import List, Set
from python.datastructure.graph.Graph import Graph
from python.datastructure.graph.readgraph import readgraph


def bfs(g: Graph, s: str) -> List[str]:
    visited = set()
    queue = [s]
    while queue:
        vertex_id = queue.pop(0)
        visited.add(vertex_id)
        for adj_vertex in g.getVertex(vertex_id).getConnections():
            if adj_vertex not in visited:
                queue.append(adj_vertex)
    return visited


if __name__ == "__main__":
    fp = '/home/peppe/Scrivania/git_repo/competitive_programming/python/python/datastructure/graph/dataset/grafo.txt'
    g = readgraph(fp)
    print(bfs(g, '8'))
