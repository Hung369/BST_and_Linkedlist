class Node:
    def __init__(self, character):
        self.character = character
        self.left = None
        self.middle = None
        self.right = None
        self.end = False


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def finding(node, key, index):
            c = key[index]
            if node is None:
                node = Node(c)
            if c < node.character:
                node.left = finding(node.left, key, index)
            elif c > node.character:
                node.right = finding(node.right, key, index)
            elif index < len(key) - 1:
                node.middle = finding(node.middle, key, index + 1)
            else:
                node.end = True
            return node
        self.root = finding(self.root, key, 0)

    def contains(self, key):
        def getting(node, key, index):
            if node is None:
                return None
            c = key[index]
            if c < node.character:
                return getting(node.left, key, index)
            elif c > node.character:
                return getting(node.right, key, index)
            elif index < len(key) - 1:
                return getting(node.middle, key, index + 1)
            else:
                return node
        node = getting(self.root, key, 0)
        if node is None:
            return False
        return node.end

    def traverse(self):
        def _traverse(node, prefix):
            if node is not None:
                _traverse(node.left, prefix)
                if node.end:
                    print(prefix + node.character)
                _traverse(node.middle, prefix + node.character)
                _traverse(node.right, prefix)
        _traverse(self.root, "")
