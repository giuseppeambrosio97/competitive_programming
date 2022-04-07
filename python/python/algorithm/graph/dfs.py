from typing import List, Set
from python.datastructure.graph.Graph import Graph
from python.datastructure.graph.readgraph import readgraph


def dfs_recursive(g: Graph, s: str, visited: Set[str]) -> List[str]:
    """
    This function perform a dfs (recursive) on the given graph g starting from the source node s.
    It's return a list of reachable vertices from s.

    Args:
        g (Graph): 
        s (str): source
        visited (Set[str]): set of visited nodes until now

    Returns:
        List[str]: list of reachable vertices from vertex s
    """
    if s not in visited:
        visited.add(s)
        for v in g.getVertex(s).getConnections():
            dfs_recursive(g, v, visited)
    return visited


def dfs_stack(g: Graph, s: str) -> List[str]:
    """
    This function perform a dfs (using a stack) on the given graph g starting from the source node s.
    It's return a list of reachable vertices from s.

    Args:
        g (Graph)
        s (str): source

    Returns:
        List[str]: list of reachable vertices from vertex s
    """
    stack = [s]
    visited = set()

    while stack:
        vertex_id = stack.pop()
        visited.add(vertex_id)
        for adj_vertex in g.getVertex(vertex_id).getConnections():
            if adj_vertex not in visited:
                stack.append(adj_vertex)

    return visited


if __name__ == "__main__":
    fp = '/home/peppe/Scrivania/git_repo/competitive_programming/python/python/datastructure/graph/dataset/grafo.txt'
    g = readgraph(fp)
    print(dfs_recursive(g, '8', set()))
    print(dfs_stack(g,'8'))
