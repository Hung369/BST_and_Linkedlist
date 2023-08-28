from Collections import *


def CreateList():
    head = LinkedList()
    num = int(input('Nhập số lượng node: '))
    for i in range(num):
        value = int(input(f'Nhập giá trị thứ {i+1}: '))
        head.AtEnd(value)

    head.listprint()
    return head


def BinaryTree():
    root = BST()
    num = int(input('Nhập số lượng node: '))
    for i in range(num):
        value = int(input(f'Nhập giá trị thứ {i+1}: '))
        root.Append(value)

    root.FirstOrder()
    return root


if __name__ == "__main__":
    root = BinaryTree()
    num = 1
    print("\n------------------------\n")
    if root.SearchValue(num):
        print(f"{num} is available in the Binary Search Tree")
    print(f"The maximum value in BST is {root.MaxNode()}")
    print(f"The minimum value in BST is {root.MinNode()}")
    print(f"BST height is {root.Height()}")
    print(f"BST total values {root.TreeVal(root)}")
    print(f"BST sum all leaf nodes {root.Sum_All_Leaf_Nodes()}")
