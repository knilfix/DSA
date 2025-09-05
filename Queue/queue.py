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
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.item


class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def print_queue(self):
        print(self.items)


# Test your LinkedListQueue
llq = LinkedListQueue()
print("Initial queue is empty:", llq.is_empty())  # Should be True

llq.enqueue("Customer A")
llq.enqueue("Customer B")
llq.enqueue("Customer C")

print("Peek at the front:", llq.peek())  # Who should be first?
print("Dequeue:", llq.dequeue())  # Who should be removed?

llq.enqueue("Customer D")
print("Dequeue:", llq.dequeue())
print("Dequeue:", llq.dequeue())
print("Dequeue:", llq.dequeue())  # What happens here?
print("Final check is empty:", llq.is_empty())
