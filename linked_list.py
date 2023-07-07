class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """Delete node with a given key.
        If key is head, delete head. Else, delete node with given key."""
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        """Delete node at a given position.
        If position is 0, delete first node.
        Else, delete node at given position."""
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


if __name__ == "__main__":
    mylinkedlist = LinkedList()
    mylinkedlist.append("A")
    mylinkedlist.append("B")
    mylinkedlist.append("C")
    mylinkedlist.append("D")

    # print("Before:")
    # mylinkedlist.print_list()
    # print("-" * 20)
    # mylinkedlist.append("D")
    # print("After: ")
    # mylinkedlist.print_list()

    # mylinkedlist.prepend("D")

    # mylinkedlist.insert_after_node(mylinkedlist.head.next, "D")

    # mylinkedlist.delete_node("B")
    # mylinkedlist.delete_node("E")

    # mylinkedlist.delete_node_at_pos(0)

    # mylinkedlist.print_list()

    # print(mylinkedlist.len_iterative())

    print(mylinkedlist.len_recursive(mylinkedlist.head))
