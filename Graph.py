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
