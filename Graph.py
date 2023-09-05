from collections import deque
from EdgePrioQueue import EdgePQ
from collections import defaultdict


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

    def getInfo(self):
        return [self.v, self.w, self.weight]

    def __str__(self):
        string = f"start:{self.v}, end:{self.w}, weight:{self.weight}"
        return string


class WeightedGraph:
    def __init__(self, v):
        self.__V = v
        self.__adj = {}
        self.__edg = []
        for i in range(self.__V):
            self.__adj[i] = set()

    def addEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.__adj[v].add(edge)
        self.__adj[w].add(edge)
        self.__edg.append(edge.getInfo())

    def adjacent(self, v):
        for e in self.__adj[v]:
            print(e)

    def num_Of_Vertex(self):
        return self.__V

    def show_graph(self):
        for i in range(self.__V):
            print(f"Vertex {i}:")
            for e in self.__adj[i]:
                print(e)

    def find(self, parent, i):  # detect acyclic path functions
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # performs the union of two subsets x and y using the union by rank method.
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_MST(self):
        result = []
        i, e = 0, 0
        # sorts all wetghts in ascending order
        self.__edg = sorted(self.__edg, key=lambda item: item[2])
        parent = []
        rank = [0]*self.__V  # union find

        for node in range(self.__V):  # initialize the connected path
            parent.append(node)

        while e < self.__V - 1:
            u, v, w = self.__edg[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:  # do not have an acyclic path then add into the tree
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")

    def prim_MST(self):
        result = []
        visited = [False]*self.__V
        pq = EdgePriorityQueue()
        self.__visit(0, visited, pq)
        while not pq.isEmpty():
            edge = pq.remove()
            v = edge.either()
            w = edge.other(v)
            if visited[v] and visited[w]:
                continue
            result.append(edge.getInfo())
            if not visited[v]:
                self.__visit(v, visited, pq)
            if not visited[w]:
                self.__visit(w, visited, pq)
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")

    def __visit(self, vertex, visited, pq):
        visited[vertex] = True
        for e in self.__adj[vertex]:
            if not visited[e.other(vertex)]:
                pq.insert(e)


class EdgePriorityQueue(EdgePQ):
    def __init__(self):
        super().__init__()

    def insert(self, edge):
        self.queue.put((edge.weight, edge))

    def remove(self):
        if not self.queue.empty():
            # Return the edge object, not the priority
            return self.queue.get()[1]
        else:
            return None


class DirectedEdge:
    def __init__(self, start, end, weight):
        self.__v = start
        self.__w = end
        self.__weight = weight

    def getFrom(self):
        return self.__v

    def getTo(self):
        return self.__w

    def getWeight(self):
        return self.__weight

    def getInfo(self):
        return self.__v, self.__w, self.__weight

    def __str__(self):
        string = f"{self.__v} --> {self.__w}, weight:{self.__weight}"
        return string


class WeightedDigraph:
    def __init__(self, number):
        self.__V = number
        self.__adj = {}
        for vertex in range(self.__V):
            self.__adj[vertex] = set()

    def addEdge(self, edge):
        v = edge.getFrom()
        self.__adj[v].add(edge)

    def num_Of_Vertex(self):
        return self.__V

    def adjacent(self, v):
        for e in self.__adj[v]:
            print(e)

    def adj(self, v):
        return self.__adj[v]

    def show_graph(self):
        for i in range(self.__V):
            print(f"Vertex {i}:")
            for e in self.__adj[i]:
                print(e)


class SP():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
