# Data structure and Algo: Stack
class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []  # returns True if empty otherwise False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self) -> list:
        return self.items
