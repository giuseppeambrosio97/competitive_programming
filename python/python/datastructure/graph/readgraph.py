from python.datastructure.graph.Graph import Graph


def readgraph(filename):
    with open(filename, 'r') as f:
        edges = f.readlines()

    g = Graph()

    for edge in edges:
        edge = edge.replace('\n', '').split(' ')
        g.addEdge(edge[0], edge[1], 1)

    return g


if __name__ == '__main__':
    print(readgraph('python/datastructure/graph/dataset/grafo.txt'))
