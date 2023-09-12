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
        self.root = self._put(self.root, key, 0)

    def _put(self, node, key, index):
        c = key[index]
        if node is None:
            node = Node(c)
        if c < node.character:
            node.left = self._put(node.left, key, index)
        elif c > node.character:
            node.right = self._put(node.right, key, index)
        elif index < len(key) - 1:
            node.middle = self._put(node.middle, key, index + 1)
        else:
            node.end = True
        return node

    def contains(self, key):
        node = self._get(self.root, key, 0)
        if node is None:
            return False
        return node.end

    def _get(self, node, key, index):
        if node is None:
            return None
        c = key[index]
        if c < node.character:
            return self._get(node.left, key, index)
        elif c > node.character:
            return self._get(node.right, key, index)
        elif index < len(key) - 1:
            return self._get(node.middle, key, index + 1)
        else:
            return node
