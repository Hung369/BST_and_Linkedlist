from NodesLib import *
from Graph import *
from Sorting import SortArray
from TSearchTree import TernarySearchTree


def SinglyLinkedList():
    head = LinkedList()
    num = int(input('Enter numbers of nodes: '))
    for i in range(num):
        value = int(input(f'Enter the int value #{i+1}: '))
        head.AtEnd(value)

    head.listprint()
    head.insert(position=2, value=10)
    print("\n-------------------\n")
    print("List after insert new value")
    head.listprint()
    num = 7
    head.delete_all_values(num)
    print(f"\nList after delete all {num} values\n")
    head.listprint()
    return head


def BinaryTree():
    root = BST()
    num = int(input('Enter numbers of nodes: '))
    for i in range(num):
        value = int(input(f'Enter the int value #{i+1}: '))
        root.Append(value)

    root.FirstOrder()

    num = 1
    print("\n------------------------\n")
    if root.SearchValue(num):
        print(f"{num} is available in the Binary Search Tree")
    print(f"The maximum value in BST is {root.MaxNode()}")
    print(f"The minimum value in BST is {root.MinNode()}")
    print(f"BST height is {root.Height()}")
    print(f"BST total values {root.TreeVal()}")
    print(f"BST sum all leaf nodes {root.Sum_All_Leaf_Nodes()}")
    return root


def Undirected():
    graph = Undirected_Graph(13)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 6)
    graph.addEdge(0, 5)
    graph.addEdge(5, 3)
    graph.addEdge(5, 4)
    graph.addEdge(3, 4)
    graph.addEdge(4, 6)
    graph.addEdge(7, 8)
    graph.addEdge(9, 10)
    graph.addEdge(9, 11)
    graph.addEdge(9, 12)
    graph.addEdge(11, 12)
    print(f"Number of vertices in graph is {graph.num_Of_Vertex()}")
    print("Graph in adjacency-list \n")
    print(graph.show_graph())
    print("\n-----------------------------\n")
    print("DFS Traversal")
    graph.DFS_Path(0)
    cc = graph.connected_components()
    print("\n-----------------------------\n")
    print("All connected components in the graph \n")
    print(cc)
    if (graph.isCyclicConnected(0)):
        print("\nThe graph has cyclic path.")


def DirectGraph():
    digraph = Directed_Graph(7)
    digraph.addEdge(0, 1)
    digraph.addEdge(0, 2)
    digraph.addEdge(0, 3)
    digraph.addEdge(0, 4)
    digraph.addEdge(1, 2)
    digraph.addEdge(1, 3)
    digraph.addEdge(1, 5)
    digraph.addEdge(2, 3)
    digraph.addEdge(3, 4)
    digraph.addEdge(3, 5)
    digraph.addEdge(3, 6)
    digraph.addEdge(4, 6)
    print(f"Number of vertices in graph is {digraph.num_Of_Vertex()}")
    print("Graph in adjacency-list \n")
    print(digraph.show_graph())
    print("\n-----------------------------\n")
    print("DFS Traversal")
    digraph.DFStraverse(0)
    print("\n-----------------------------\n")
    arr = digraph.TopoSort()
    print("Digraph Topological Sort")
    print(arr)
    print("\n-----------------------------\n")


def WGraph():
    myfile = open('weightgraph.txt', 'r')
    text = myfile.read()
    myfile.close()
    comps = text.split('\n')
    vertex, edges = comps[0], comps[1]

    wgraph = WeightedGraph(int(vertex))

    comps.pop(0)
    comps.pop(0)
    for i in range(int(edges)):
        start, end, weight = comps[i].split()
        e = EdgeWeight(int(start), int(end), float(weight))
        wgraph.addEdge(e)

    wgraph.show_graph()
    print("\n-----------------------------\n")
    print("Kruskal MST\n")
    wgraph.kruskal_MST()
    print("\n-----------------------------\n")
    print("Prim MST\n")
    wgraph.prim_MST()


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)
                                   ] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations,
                           key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


def Shortest():
    graph = SP()
    edges = [
        ('X', 'A', 7),
        ('X', 'B', 2),
        ('X', 'C', 3),
        ('X', 'E', 4),
        ('A', 'B', 3),
        ('A', 'D', 4),
        ('B', 'D', 4),
        ('B', 'H', 5),
        ('C', 'L', 2),
        ('D', 'F', 1),
        ('F', 'H', 3),
        ('G', 'H', 2),
        ('G', 'Y', 2),
        ('I', 'J', 6),
        ('I', 'K', 4),
        ('I', 'L', 4),
        ('J', 'L', 1),
        ('K', 'Y', 5),
    ]

    for edge in edges:
        graph.add_edge(*edge)
    print(dijsktra(graph, 'X', 'Y'))


def sortarr():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sortin = SortArray(arr)
    print(sortin.mergesort())


def storeWord():
    tentree = TernarySearchTree()
    tentree.insert("cat")
    tentree.insert("cats")
    tentree.insert("up")
    tentree.insert("bug")
    print(tentree.contains("cat"))
    tentree.traverse()


if __name__ == "__main__":
    storeWord()
