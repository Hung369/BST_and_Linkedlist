# This is Ternary Search Tree. The data structure for storing words and strings.

class NodeThree:
    def __init__(self, value):
        self.char = value
        self.left = self.right = self.equal = None
        self.isEnd = False


class TST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        def traversal(word, current):
            if current is None:
                current = NodeThree(word[0])
            if word[0] < current.char:
                current.left = traversal(current.left, word)
            elif word > current.char:
                current.right = traversal(current.right, word)
            elif len(word) > 1:
                current.middle = traversal(current.middle, word[1:])
            else:
                current.isEnd = True
            return current
        self.root = traversal(word, self.root)

    def SearchTST(self, word):
        def finding(word, current):
            if current is None:
                return False
            if word[0] < current.char:
                return finding(word, current.left)
            elif word[0] > current.char:
                return finding(word, current.right)
            elif len(word) > 1:
                return finding(word, current.equal)
            else:
                return current.isEnd
        result = finding(word, self.root)
        return result

    def traverseTST(self):
        def traverseTSTUtil(root, buffer, depth):
            if root:
                traverseTSTUtil(root.left, buffer, depth)
                buffer[depth] = root.char
                if root.isEndOfString:
                    print("".join(buffer[:depth+1]))
                traverseTSTUtil(root.equal, buffer, depth+1)
                traverseTSTUtil(root.right, buffer, depth)

        buffer = [''] * 50
        traverseTSTUtil(self.root, buffer, 0)
