class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.leftChild = None
        self.rightChild = None

    # def __str__(self) -> None:
    #     return "Node=" + self.value


class Tree:
    def insert(value: int):
        node = Node(value)

        if root is None:
            root = node
            return

        current = node
        while True:
            if value < current.value:
                if current.leftChild is None:
                    current.leftChild = node
                    break
                current = current.leftChild
            else:
                if current.rightChild is None:
                    current.rightChild = node
                    break
                current = current.rightChild


if __name__ == "__main__":
    myTree = Tree()
    Tree.insert(1)
