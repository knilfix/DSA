class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def prepend(self, item):
        new_node = Node(item)

        # if list is empty
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def delete_tail(self):
        if self.is_empty():
            return None

        old_tail = self.tail

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = old_tail.prev
            self.tail.next = None
            old_tail.prev = None

        self.size -= 1
        return old_tail.data

    def is_empty(self):
        return self.head is None


# Test our Doubly Linked List
dll = DoublyLinkedList()
print("List created. Empty?", dll.is_empty())

dll.append("A")
dll.append("B")
dll.prepend("First")
# List should now be: First <-> A <-> B

print("Head:", dll.head.data)  # Should be?
print("Tail:", dll.tail.data)  # Should be?
print("Size:", dll.size)  # Should be?

# Let's delete from the tail
removed = dll.delete_tail()
print("Removed from tail:", removed)  # Should be?
print("New Tail:", dll.tail.data)  # Should be?
print("New Size:", dll.size)  # Should be?
