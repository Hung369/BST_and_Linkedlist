from collections import deque


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

    def DFS_Path(self, v):
        visited = set()
        self.__dfs(visited, v)

    def __dfs(self, visited, v):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.__adj[v]:
            if neighbour not in visited:
                self.__dfs(visited, neighbour)

    def degree(self, v):
        degree = 0
        for i in self.__adj[v]:
            degree += 1
        return degree

    def maximum_degree(self):
        maxim = 0
        for v in range(self.__V):
            tmp = self.degree(self.__adj[v])
            if tmp > maxim:
                maxim = tmp
        return maxim

    def connected_components(self):
        visited = set()
        cc = []
        for v in range(self.__V):
            if v not in visited:
                temp = []
                cc.append(self.__traversal(temp, visited, v))
        return cc

    def __traversal(self, temp, visited, v):
        visited.add(v)
        temp.append(v)
        for neighbour in self.__adj[v]:
            if neighbour not in visited:
                temp = self.__traversal(temp, visited, neighbour)
        return temp

    def isCyclicConnected(self, started):
        parent = [-1] * self.__V
        visited = [False] * self.__V

        # Create a queue for BFS
        q = deque()

        # Mark the current node as
        # visited and enqueue it
        visited[started] = True
        q.append(started)

        while len(q) != 0:  # BFS traversal

            # Dequeue a vertex from queue and check all adjacent nodes
            u = q.pop()

            for v in self.__adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    parent[v] = u
                elif parent[u] != v:
                    return True

        return False


class Directed_Graph:
    def __init__(self, number):
        self.__V = number
        self.__adj = {}
        for vertex in range(self.__V):
            self.__adj[vertex] = set()

    def addEdge(self, v, w):
        if v not in self.__adj and w not in self.__adj:
            self.__V += 1
        self.__adj[v].add(w)

    def adjacent(self, v):
        return self.__adj[v]

    def num_Of_Vertex(self):
        return self.__V

    def show_graph(self):
        return self.__adj

    def DFStraverse(self, v):
        visited = [False] * self.num_Of_Vertex()
        self.__dfs(visited, v)

    def __dfs(self, visited, start):
        visited[start] = True
        print(start, end=" ")
        for vertex in self.__adj[start]:
            if not visited[vertex]:
                self.__dfs(visited, vertex)

    def TopoSort(self):
        visited = [False] * self.num_Of_Vertex()
        stack = list()
        for vertex in range(self.num_Of_Vertex()):
            if not visited[vertex]:
                self.__traversal(vertex, visited, stack)
        return stack[::-1]

    def __traversal(self, vertex, visited, stack):
        visited[vertex] = True
        for v in self.__adj[vertex]:
            if not visited[v]:
                self.__traversal(v, visited, stack)
        stack.append(vertex)

    def strong_connected(self, v, w):
        if w in self.__adj[v] and v in self.__adj[w]:
            return True
        return False


class EdgeWeight:
    def __init__(self, vertex, end, value):
        self.v = vertex
        self.w = end
        self.weight = value

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        return self.v

    def compareTo(self, that):
        if self.weight < that.weight:
            return -1
        elif self.weight > that.weight:
            return 1
        return 0

    def __str__(self):
        string = f"start:{self.v}, end:{self.w}, weight:{self.weight}"
        return string


class WeightedGraph:
    def __init__(self, v):
        self.__V = v
        self.__adj = {}
        for i in range(self.__V):
            self.__adj[i] = set()

    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.__adj[v].add(edge)
        self.__adj[w].add(edge)

    def adjacent(self, v):
        for e in self.__adj:
            print(e)

    def num_Of_Vertex(self):
        return self.__V

    def show_graph(self):
        for i in range(self.__V):
            print(f"Vertex {i}:")
            for e in self.__adj[i]:
                print(e)
