import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def __lt__(self, nxt):
        return self.freq < nxt.freq

class HuffmanCoding:
    def __init__(self, string):
       self.text = string
       self.char_freq = self.get_key()
       self.root = None
       self.huffmancode = {}

    def get_key(self):
        frequency = Counter(self.text)
        print("\nResult:")
        print("Characters\tFrequency")
        for char, freq in frequency.items():
            print(f"{char}\t\t{freq}")
        return frequency
    
    def buildTree(self):
        listNode = [Node(char, freq) for char, freq in self.char_freq.items()]
        heapq.heapify(listNode)

        while len(listNode) != 1:
            left = heapq.heappop(listNode)
            right = heapq.heappop(listNode)

            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right

            heapq.heappush(listNode, parent)

        self.root = listNode[0]
    

    def buildHuffManCode(self):
        def digitalize(curentnode, binary_string='', huff_code={}):
            if curentnode is None:
                return

            if curentnode.char is not None:
                huff_code[curentnode.char] = binary_string

            digitalize(curentnode.left, binary_string + '0', huff_code)
            digitalize(curentnode.right, binary_string + '1', huff_code)
            return huff_code
        self.huffmancode = digitalize(self.root)
        return self.huffmancode
    
    def decode_huff(self, encoded_text):
        current_node = self.root
        decoded_text = ''

        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.is_leaf() is True:
                decoded_text += current_node.char
                current_node = self.root

        return decoded_text
