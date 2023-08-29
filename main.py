from Collections import *
from Graph import *


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


if __name__ == "__main__":
    Undirected()
