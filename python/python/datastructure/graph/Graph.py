from python.datastructure.graph.Vertex import Vertex


class Graph():
    def __init__(self):
        self.vertices = {}

    def getVertex(self, v):
        return self.vertices.get(v)

    def addEdge(self, vertex1, vertex2, weight):
        if self.vertices.get(vertex1) is None:
            self.vertices[vertex1] = Vertex(vertex1)
        if self.vertices.get(vertex2) is None:
            self.vertices[vertex2] = Vertex(vertex2)

        self.vertices[vertex1].addConnection(vertex2, weight)

    def getVertices(self):
        return list(self.vertices.keys())

    def __str__(self):
        str_ = f'Vertices: {self.getVertices()}\n\n'
        for i,(_, vertex) in enumerate(self.vertices.items()):
            str_ += f'{i})\n{vertex}'

        return str_


