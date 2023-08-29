class Undirected_Graph:
    def __init__(self, number):
        self.V = number
        self.adj = {}
        for vertex in range(self.V):
            self.adj[vertex] = set()

    def addEdge(self, v, w):
        if not (self.adj.has_key(v) and self.adj.has_key(v)):
            self.V += 1
        self.adj[v].add(w)
        self.adj[w].add(v)

    def adjacent(self, v):
        return self.adj[v]

    def num_Of_Vertex(self):
        return self.V
