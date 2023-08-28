import math


class Node:  # init node class
    def __init__(self, dataval):
        self.value = dataval

    def getVal(self):
        return self.value


class ListNode(Node):  # node class for linked list
    def __init__(self, dataval):
        super().__init__(dataval)
        self.next = None


class LinkedList:  # singly linked list class
    def __init__(self):
        self.head = None

    def AtEnd(self, newdata):
        NewNode = ListNode(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = NewNode

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.getVal())
            printval = printval.next


class TreeNode(Node):  # Binary Tree node
    def __init__(self, dataval):
        super().__init__(dataval)
        self.left = None
        self.right = None


class BST:  # Binary Search Tree class
    def __init__(self):
        self.root = None

    def Append(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        else:
            self.insert(value, self.root)

    def insert(self, data, current_node):
        if data < current_node.getVal():
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self.insert(data, current_node.left)
        elif data > current_node.getVal():
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self.insert(data, current_node.right)
        else:
            print("Value already in tree")

    def FirstOrder(self):
        if self.root is not None:
            self.first_order_traversal(self.root)

    def first_order_traversal(self, current_node):
        if current_node is not None:
            print(current_node.getVal())
            self.first_order_traversal(current_node.left)
            self.first_order_traversal(current_node.right)

    # traverse the node from root to right recursively until the right is NULL.
    def MaxNode(self):
        if self.root is None:
            print("Root isn't available")
        else:
            pointer = self.root
            while pointer.right is not None:
                pointer = pointer.right
            return pointer.getVal()

    # traverse the node from root to left recursively until the left is NULL.
    def MinNode(self):
        if self.root is None:
            print("Root isn't available")
        else:
            pointer = self.root
            while pointer.left is not None:
                pointer = pointer.left
            return pointer.getVal()

    def SearchValue(self, value):
        if self.root is None:
            print("Root isn't available")
        else:
            pointer = self.root
            boolean = self.finding_node(pointer, value=value)
            return boolean

    def finding_node(self, pointer, value):  # binary search
        if not pointer:
            return False
        if pointer.getVal() == value:
            return True
        if pointer.getVal() > value:
            return self.finding_node(pointer.left, value)
        return self.finding_node(pointer.right, value)

    def Height(self):
        if self.root is None:
            return 0
        else:
            pointer = self.root
            height = self.Depth(pointer)
            return height

    def Depth(self, node):  # calculate BST height
        if node is None:
            return 0
        leftDepth = self.Depth(node.left)
        rigthDepth = self.Depth(node.right)
        return max(leftDepth, rigthDepth) + 1

    def TreeVal(self):  # sum all nodes on the tree
        if self.root is None:
            return 0
        return self.root.getVal() + self.TreeVal(self.root.left) + self.TreeVal(self.root.right)

    def Sum_All_Nodes_on_K_level(self, k):  # sum all the nodes at k level
        if self.root is None:
            return 0
        if k == 0:
            return self.root.getVal()
        return self.Sum_All_Nodes_on_K_level(self.root.left, k-1) + self. Sum_All_Nodes_on_K_level(self.root.right, k-1)

    def Sum_All_Leaf_Nodes(self):
        if self.root is None:
            return 0
        if self.root.left is None and self.root.right is None:
            return self.root.getVal()
        return self.Sum_All_Leaf_Nodes(self.root.left) + self.Sum_All_Leaf_Nodes(self.root.right)
