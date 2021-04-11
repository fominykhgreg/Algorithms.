"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter


class Node:
    def __init__(self, data=None, children=[]):
        self.data = data
        self.children = children
        self._code = 0
        self.root = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value
        self._is_leaf = len(value) == 0

    @property
    def is_leaf(self):
        return self._is_leaf

    def set_codes(self, parent_code='', is_left=True):
        self.code = f"{parent_code}{0 if is_left else 1}"

        if self.is_leaf:
            self.code = self.code[1:]

        if len(self.children):
            self.children[0].set_codes(self.code, True)
            self.children[1].set_codes(self.code, False)

    def traverse_df(self, callback):
        for x in self.children:
            callback(x)
            x.traverse_df(callback)

    def find_leaf(self, code):
        if self.is_leaf:
            return self
        else:
            first = code[1]
            other = code[1:]
            if first == '0':
                return self.children[0].find_leaf(other)
            else:
                return self.children[1].find_leaf(other)


def get_frequency(s: str):
    return reversed(Counter(s).most_common())


def idx_to_insert(ls: list, freq: int):
    res = len(ls)
    for i, x in enumerate(ls):
        if x[1] >= freq:
            res = i
            break
    return res


code_table = {}


def fill_table(n: Node):
    if n.is_leaf:
        code_table[n.data] = n.code


string = 'beep boop beer!'

stck = list(get_frequency(string))

while len(stck) > 2:
    c1 = stck.pop(0)
    c2 = stck.pop(0)
    v1 = c1[0]
    v2 = c2[0]
    f1 = c1[1]
    f2 = c2[1]
    n1 = Node(v1) if not isinstance(v1, Node) else v1
    n2 = Node(v2) if not isinstance(v2, Node) else v2
    n = Node(children = [n1, n2])
    idx = idx_to_insert(stck, f1+f2)
    stck.insert(idx, (n, f1+f2))

root = Node(children = [stck[0][0], stck[1][0]])

root.set_codes()
root.traverse_df(fill_table)

print('Строка:\n', string, sep = '')

print('Таблица кодов:')
for k in code_table:
    print(f'{k}:', code_table[k])
print("*" * 100)
print('Закодированная строка:')
encoded_str = ' '.join(map(lambda x: code_table[x], string))
print(encoded_str)
print("*" * 100)
print('Декодированная строка:')
decoded_str = ''.join(map(lambda x: root.find_leaf(f'0{x}').data, encoded_str.split(' ')))

print(decoded_str)
print("*" * 100)
