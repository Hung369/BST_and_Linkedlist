import heapq
from collections import Counter

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

            if current_node.is_leaf():
                decoded_text += current_node.char
                current_node = self.root

        return decoded_text

class LZW:    
    def setting(self):
        self.dictionary = {chr(i):i for i in range(256)}
        self.next = 256
        self.dedict = {i:chr(i) for i in range(256) }
        
    
    def compression(self, data):
        self.setting()
        result = []
        sequence = ""

        for char in data:
            new_sequence = sequence + char
            if new_sequence in self.dictionary:
                sequence = new_sequence
            else:
                result.append(self.dictionary[sequence])
                self.dictionary[new_sequence] = self.next
                self.next += 1
                sequence = char

        result.append(self.dictionary[sequence])
        return result
    
    def decompression(self, data):
        self.setting()
        result = [chr(data[0])]
        sequence = result[0]

        for code in data[1:]:
            if code in self.dedict:
                entry = self.dedict[code]
            elif code == next_code:
                entry = sequence + sequence[0]
            else:
                raise ValueError("Invalid compressed data")

            result.append(entry)
            self.dedict[next_code] = sequence + entry[0]
            next_code += 1
            sequence = entry

        return "".join(result)
