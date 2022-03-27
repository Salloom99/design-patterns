class Node:
    def __init__(self, value) -> None:
        self.value = value

    def print(self):
        print(self.value)


class Branch(Node):
    def __init__(self, value, right, left) -> None:
        super().__init__(value)
        self.left_leaf = left
        self.right_leaf = right

    def print(self):
        self.left_leaf.print()
        self.right_leaf.print()
        return super().print()


class Leaf(Node):
    def print(self):
        return super().print()


class BTree:
    def __init__(self, root) -> None:
        self.root = root

    def print(self):
        self.root.print()

def CompositePattern():
    node7 = Leaf('7')
    node6 = Leaf('6')
    node5 = Leaf('5')
    node4 = Leaf('4')
    node3 = Branch('3',node6,node7)
    node2 = Branch('2',node4,node5)
    node1 = Branch('1',node2,node3)
    tree = BTree(node1)
    tree.print()