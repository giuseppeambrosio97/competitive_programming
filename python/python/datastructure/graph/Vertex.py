class Vertex():
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def getId(self):
        return self.key

    def getConnections(self):
        return list(self.connections.keys())

    def addConnection(self, v, weight):
        self.connections[v] = weight

    def getWeight(self, nbr):
        return self.connections.get(nbr)

    def __str__(self):
        str_ = f'Vertex ID: {self.key}\n'
        if len(self.connections):
            str_ += 'Neighbors:\n'
            for adj_vertex, weight in self.connections.items():
                str_ += f'-> Vertex: {adj_vertex} - Weight: {weight}\n'
        else:
            str_ += 'NO CONNECTIONS\n'
        return str_


if __name__ == '__main__':
    vertex = Vertex('8')

    vertex.addConnection('1', 2)
    vertex.addConnection('4', 1)

    print(vertex)
    print('*'*30)
    print(vertex.getConnections())
    print('*'*30)
    print(vertex.getWeight('1'))
    print('*'*30)
    print(vertex.getId())





