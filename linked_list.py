from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_beginning(self):
        if not self.head:
            print("No steps to remove at the beginning!")
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        if not self.head:
            print("No steps to remove at the end!")
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return removed_data

    def remove_at(self, data):
        if not self.head:
            print("No steps to remove!")
            return None
        if self.head.data == data:
            self.head = self.head.next
            return data
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:
            print(f"'{data}' not found in list.")
            return None
        removed_data = current.next.data
        current.next = current.next.next
        return removed_data

    def display(self):
        if not self.head:
            print("No steps available.")
            return
        current = self.head
        step = 1
        while current:
            print(f"Step {step}: {current.data}")
            current = current.next
            step += 1
