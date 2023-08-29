class Undirected_Graph:
    def __init__(self, number):
        self.__V = number
        self.__adj = {}
        for vertex in range(self.__V):
            self.__adj[vertex] = set()

    def addEdge(self, v, w):
        if v not in self.__adj and w not in self.__adj:
            self.__V += 1
        self.__adj[v].add(w)
        self.__adj[w].add(v)

    def adjacent(self, v):
        return self.__adj[v]

    def num_Of_Vertex(self):
        return self.__V

    def show_graph(self):
        return self.__adj
