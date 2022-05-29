"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""

from collections import Counter


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'(Node [{self.value} {self.left} {self.right}])'


class HuffmanTree:
    def __init__(self, tree):
        self.root = tree
        self.buffer = []
        self.codes = {}

    def _insert_buffer(self, index, code):
        if len(self.buffer) >= index + 1:
            self.buffer[index] = code
        else:
            self.buffer.append(code)

    def huffman_walk(self, tree, length):
        node = tree
        if not node:
            return
        elif isinstance(node, str):
            self.codes[node] = ''.join(map(str, self.buffer[0: length]))
            return
        self._insert_buffer(index=length, code=0)
        self.huffman_walk(node.left, length + 1)
        self._insert_buffer(index=length, code=1)
        self.huffman_walk(node.right, length + 1)

    def generate_code(self):
        self.huffman_walk(self.root, 0)


def get_huffman_tree(string_to_tree):
    counted_chars = Counter(string_to_tree)
    values = sorted(counted_chars, key=counted_chars.get, reverse=True)
    weight = [counted_chars[key] for key in values]

    while len(values) > 1:
        sum_weight = 0
        left = values.pop()
        right = values.pop()
        for _ in range(2):
            sum_weight += weight.pop()
        n = Node(value=None, left=left, right=right)

        for i in range(len(values) - 1, -1, -1):
            if sum_weight <= weight[i]:
                weight.insert(i + 1, sum_weight)
                values.insert(i + 1, n)
                break
        else:
            weight.insert(0, sum_weight)
            values.insert(0, n)

    return values[0]


if __name__ == '__main__':
    s = 'beep boop beer!'

    h_tree = HuffmanTree(tree=get_huffman_tree(s))
    h_tree.generate_code()
    s_encoded = ''
    for char in s:
        s_encoded += h_tree.codes[char]
    print(f'Таблица кодирования: {h_tree.codes}')
    print(f'Закодированная строка: {s_encoded}')
