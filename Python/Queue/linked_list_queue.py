class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        dequeued_item = self.head.item

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.size -= 1
        return dequeued_item

    def is_empty(self):
        return self.tail is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.item

    def print_queue(self):
        if self.is_empty():
            print("[]")
            return

        print("[")
        current = self.head
        while current:
            print(f" {current.item}")
            current = current.next

        print("]")
        pass
