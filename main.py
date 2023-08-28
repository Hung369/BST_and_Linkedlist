from Collections import *


def SinglyLinkedList():
    head = LinkedList()
    num = int(input('Enter numbers of nodes: '))
    for i in range(num):
        value = int(input(f'Enter the int value #{i+1}: '))
        head.AtEnd(value)

    head.listprint()
    head = head.insert(5, 10)
    print("List after insert new value")
    head.listprint()
    num = 3
    head = head.delete_all_values(num)
    print(f"List after delete all {num} values")
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


if __name__ == "__main__":
    head = SinglyLinkedList()
