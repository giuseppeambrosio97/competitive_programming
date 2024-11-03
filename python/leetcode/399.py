from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional


@dataclass
class Edge:
    node_name: str
    weight: float


@dataclass
class Node:
    name: str
    out_edges: List[Edge] = field(default_factory=list)
    in_edges: List[Edge] = field(default_factory=list)


@dataclass
class Graph:
    nodes: Dict[str, Node]


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        
        def build_graph(equations: List[List[str]], values: List[float]) -> Graph:
            nodes: Dict[str, Node] = {}
            for (numerator, denominator), value in zip(equations, values):
                if numerator not in nodes:
                    nodes[numerator] = Node(name=numerator)
                if denominator not in nodes:
                    nodes[denominator] = Node(name=denominator)
                # Add directed edges for numerator -> denominator and denominator -> numerator
                nodes[numerator].out_edges.append(Edge(node_name=denominator, weight=value))
                nodes[denominator].out_edges.append(Edge(node_name=numerator, weight=1 / value))
            return Graph(nodes=nodes)

        def dfs(start: Node, target_name: str, visited: Set[str]) -> Optional[float]:
            if start.name == target_name:
                return 1.0
            visited.add(start.name)
            for edge in start.out_edges:
                if edge.node_name not in visited:
                    result = dfs(g.nodes[edge.node_name], target_name, visited)
                    if result is not None:
                        return result * edge.weight
            visited.remove(start.name)
            return None

        def compute_query(query: List[str]) -> float:
            numerator, denominator = query
            if numerator not in g.nodes or denominator not in g.nodes:
                return -1.0
            if numerator == denominator:
                return 1.0
            result = dfs(g.nodes[numerator], denominator, set())
            return result if result is not None else -1.0

        g = build_graph(equations, values)
        
        return [compute_query(query) for query in queries]
