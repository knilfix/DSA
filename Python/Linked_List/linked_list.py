class Node:
    def __init__(self, data):
        self.data = data
        self.next_node: "Node | None" = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):
        """Add node to the beginning of the list"""
        node = Node(data)
        # if list is empty
        if self.is_empty():
            self.head = node
            self.size += 1
            return

        # if list is not empty
        node.next_node = self.head
        self.head = node
        self.size += 1
        return

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            # Traverse until we find the last node
            while current is not None:
                if current.next_node is None:
                    current.next_node = node
                    break
                current = current.next_node
        self.size += 1

    def insert_after(self, target_data, data):
        """Insert node after a specific value"""

        if self.is_empty():
            print("Cannot insert after in empty list")
            return

        current = self.head
        while current is not None:
            if current.data == target_data:
                node = Node(data)
                node.next_node = current.next_node
                current.next_node = node
                self.size += 1
                return
            # continue traversal
            current = current.next_node

        print(f"Target data {target_data} not found in list")

    def delete(self, data) -> bool:
        """Delete first occurrence of data"""
        if self.is_empty():
            return False

        # if its the head
        if self.head.data == data:
            self.head = self.head.next_node
            self.size -= 1  # Don't forget to decrement size!
            return True

        prev = self.head
        current = self.head.next_node

        while current:
            if current.data == data:
                prev.next_node = current.next_node
                current.next_node = None
                self.size -= 1
                return True
            prev = current
            current = current.next_node
        return False

    def search(self, data):
        """Check if data exists in the list"""
        if self.is_empty():
            return False

        current = self.head

        while current is not None:
            if current.data == data:
                # return  true
                return True
            current = current.next_node

        return False

    def print_list(self):
        """Print all elements in the list"""
        if self.is_empty():
            print("List is empty")
            return

        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next_node

        print(" -> ".join(elements))

    def length(self) -> int:
        """Return the number of nodes"""

        return self.size

    def reverse(self):
        """Reverse the linked list"""
        if self.is_empty() or self.head.next_node is None:  # type: ignore
            return

        prev = None
        current = self.head

        while current:
            next_node = current.next_node
            current.next_node = prev

            prev = current
            current = next_node

        self.head = prev

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        # else
        return False

    def get(self, index: int):
        """Get the data at specific index (0-based)"""
        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds for size {self.size}")

        current = self.head
        for i in range(index):
            current = current.next_node
        return current.data

    def __getitem__(self, index: int):
        """Enable list-like indexing: linked_list[index]"""
        if index < 0:
            index = self.size + index  # Handle negative indices

        if index < 0 or index >= self.size:
            raise IndexError(f"Index {index} out of bounds for size {self.size}")

        return self.get(index)  # Reuse your existing get method

    def __iter__(self):
        """Make linked list iterable"""
        current = self.head
        while current:
            yield current.data
            current = current.next_node
